import flask
import sys
import werkzeug.exceptions
from flask import request
from flask import render_template

from marshmallow import Schema, fields, post_load, ValidationError

import datetime as dt

import pyg.web
from pyg.web import plugin
from pyg.web import models
from pyg.web import db


bp = flask.Blueprint('api', __name__, url_prefix='/api/v1')


@bp.route('/')
def index():
    """Return api description."""
    return "TODO:api"

@bp.route('/home')
def home():
    return render_template('index.php')

# Test route.  Delete me for production.
@bp.route('/testpost', methods=['POST'])
def test_post():
    print('shits on fire yo', file=sys.stderr)
    return(request.json['email'])

# TODO: make this take JSON instead of Form.
@bp.route('/user', methods=['POST'])
def new_user():
    """add a new user. Called from the new user page.
    Should check if the email field exists, then create a new user tied to a UserAuth
    """

    print('printing json...')
    print(request.json)

    
    class NewUserAuthSchema(Schema):
        name = fields.String()
        password = fields.String()
        email = fields.String()

        @post_load
        def make_auth(self, data, **kwargs):
            return models.UserAuth(**data)

        
    class NewPersonSchema(Schema):
        auth = fields.Nested(NewUserAuthSchema, required=False, allow_none=True, many=False)
        created = fields.DateTime()

        @post_load
        def make_person(self, data, **kwargs):
            return models.Person(**data)

        
    #call list of emails in db
    q = db.web.session.query(models.UserAuth).filter_by(email=request.json['email'])
    q = list(q)
    #check if email in db.emails
    if q:
        
        return "We found a user with that email already."
    
    else:

        schema = NewUserAuthSchema()
        # this next thing is busted.  Marshmallow wants a string json?  I dunno.  Cate is messaging so I'm outie, bro.
        loadeduserdata = schema.loads(request.json)
        newuser = models.Person(created = dt.datetime.now())
        newuser.auth = loadeduserdata
        db.web.session.add(newuser)
        db.web.session.commit()
        
        return "user successfully entered"

    
@bp.route('/login', methods=['POST'])
def login():
    """Login.  Should check if a user exists, and offer a number of things based on whether it does and whether the supplied password is correct etc."""

    #get email and password from request
    email = request.form['email']
    password = request.form['password']
    
    class AuthSchema(Schema):
        email = fields.String()
        password = fields.String()

    class PersonSchema(Schema):
        id = fields.Integer()
        auth = fields.Nested(AuthSchema, required=True, allow_none=False, many=False)

    #get the id of the user being logged in
    userauth = db.web.session.query(models.UserAuth).filter_by(email=email)

    q = list(userauth)

    print("###USERAUTH###")
    print(userauth)
    print("###LIST OF USERAUTH###")
    print(q)

    #did we find a user auth?
    if q:
        user = q[0].person
        #do the login shuffle
        #does the password match?
        if q[0].password == password:
            return "login successful as {0}. User ID is {1}".format(q[0].name,user.id)
        #TODO: send the user id# so the client just knows who's using it.
        else:
            return "password incorrect"
    else:
        return "we couldn't find a user with this email address.  Check your spelling or create a new user account."
    
