import datetime as dt
import sys

import werkzeug.exceptions
import flask
from flask import request
from flask import render_template
from flask import session
from marshmallow import Schema, fields, post_load, ValidationError

import pyg.web
from pyg.web import plugin
from pyg.web import models
from pyg.web import db


bp = flask.Blueprint('api', __name__)



# THIS IS A TEST SECTION AND SHOULD BE DELETED ALONG WITH THE FILES IT REFERENCES FOR PRODUCTION
# ################################################################################################

# This populates the db for testing purposes.  Use it as the first call in all routes until production 
def populate():
    tom = models.Person(created=dt.datetime.now())
    tom.auth = models.UserAuth(name='tom boyee', password='pass',email='chaboyee@hotmail.ru')
    tom.profile = models.UserProfile(about='My name is tom.', avatar='',birthday='every day',location='New Jersey')
    db.web.session.add(tom)
    db.web.session.commit()
    print("Database populated")
    # return "Populated the database"

# ################################################################################################
# END TEST SECTION



# Homepage
@bp.route('/')
def home():
    session['user'] = 'bob'
    return render_template('content_home.html', test=session['user'])

# Gamer profile page. 
@bp.route('/gamerprofile/<gamerid>')
def gamerprofile(gamerid):

    populate() # Testing function
    
    user = db.web.session.query(models.Person).filter_by(id=gamerid).one()
    auth = user.auth
    profile = user.profile
    
    return render_template('content_gamer_profile.html', auth=auth, profile=profile)

# Leaderboard.  Might be turned into an imported module
@bp.route('/leaderboard')
def leaderboard():
    return render_template('content_leaderboard.html')





####################################################################################################
# The following sections may or may not be the direction we're going in.  Check back on them
# once a login and signup page have been created.
# =========================
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
    
