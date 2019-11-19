import datetime as dt
import sys

import werkzeug.exceptions
import flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from marshmallow import Schema, fields, post_load, ValidationError

import pyg.web
from pyg.web import plugin
from pyg.web import models
from pyg.web import db


bp = flask.Blueprint('api', __name__)



# THIS IS A TEST SECTION AND SHOULD BE DELETED ALONG WITH THE FILES IT REFERENCES FOR PRODUCTION
# ################################################################################################

# This populates the db for testing purposes.  Use it as the first call in all routes until production
def create_new_person(person):

    print('creating new person')
    checkexists = db.web.session.query(models.UserAuth).filter_by(email=person['email'])
    checkexists = list(checkexists)

    if checkexists:
        print("user exists already")
        pass
    else:
        print("attempting to create new user")
        newperson = models.Person(created=dt.datetime.now())
        newperson.auth = models.UserAuth(name=person['name'], password=person['password'],email=person['email'])
        newperson.profile=models.UserProfile(about=person['about'], avatar=person['avatar'], birthday=person['birthday'], location=person['location'])
        db.web.session.add(newperson)
        db.web.session.commit()
        print("user entered successfully")


def populate():
    print("calling populate")
    tom = { 'name':'tom', 'password':'pass', 'email':'tom@gmail.com', 'about':'My name is tom.', 'avatar':'', 'birthday':'every day', 'location':'New Jersey'}
    create_new_person(tom)
    print("Database populated")
    # return "Populated the database"

# ################################################################################################
# END TEST SECTION



# Homepage
@bp.route('/')
def home():
    testid = ''
    return render_template('content_home.html', test=testid)


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


@bp.route('/login/<failtype>')
@bp.route('/login')
def login(failtype=None):
    populate()
    # TODO: respond to successful password by setting session variable and rerouting home
    # TODO: respond to password failure by setting attempts bit in session and allowing to try again
    # TODO: respond to email failure by responding with user not found try again
    if failtype == None:
        return render_template('login.html', failure_text="")
    elif failtype == "passworderr":
        return render_template('login.html', failure_text="Incorrect password. Please try again ")
    elif failtype == "usererr":
        return render_template('login.html', failure_text="We couldn't find that email.")
    else:
        return "unknown failure error code."

@bp.route('/authorize', methods=['POST'])
def authorize():
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
            session['userid'] = q[0].id
            return redirect('/')
            #TODO: send the user id# so the client just knows who's using it.
        else:
            return redirect('/login/passworderr')
    else:
        return redirect('/login/usererr')


