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
from pyg.web import testing
from pyg.web import auth
from pyg.web import api


bp = flask.Blueprint('api', __name__)

# Homepage
@bp.route('/')
def home():
    testid = ''
    return render_template('content_home.html', test=testid)


# Gamer profile page. 
@bp.route('/gamerprofile/<gamerid>')
def gamerprofile(gamerid):

    testing.populate() # Testing function
    
    user = db.web.session.query(models.Person).filter_by(id=gamerid).one()
    auth = user.auth
    profile = user.profile
    
    return render_template('content_gamer_profile.html', auth=auth, profile=profile)


# Leaderboard.  Might be turned into an imported module
@bp.route('/leaderboard')
def leaderboard():
    return render_template('content_leaderboard.html')


# login page.  Might become a modal later.  Gotta figure out how to do modals.
@bp.route('/login/<failtype>')
@bp.route('/login')
def login(failtype=None):
    testing.populate()

    if failtype == None:
        return render_template('login.html', failure_text="")
    elif failtype == "passworderr":
        return render_template('login.html', failure_text="Incorrect password. Please try again ")
    elif failtype == "usererr":
        return render_template('login.html', failure_text="We couldn't find that email.")
    else:
        return "unknown failure error code."


# authorization module.  Does not render a template, but redirects to login or homepage based on failure or success
@bp.route('/authorize', methods=['POST'])
def authorize():
    """Login.  Should check if a user exists, and offer a number of things based on whether it does and whether the supplied password is correct etc."""

    auth_code = auth.user(email = request.form['email'], password=request.form['password'])

    print("auth code: ", auth_code)
    
    if auth_code == "auth_success":
        # IAN: I ended up setting the 'user logged in' in the auth module.  Let me know if there's a better pattern.
        return redirect('/')
    elif auth_code == "auth_pass_err":
        return redirect('/login/passworderr')
    elif auth_code == "auth_email_err":
        return redirect('/login/usererr')
    else:
        # TODO: implement proper handler for bad auth code
        print("Bad auth code. TODO: implement proper error handler")
        return redirect('/shitsonfireyo')


# Error page.
@bp.route('/shitsonfireyo/<errortype>')
@bp.route('/shitsonfireyo')
def errorpage(errortype=None):
    return render_template('errorpage.html', errortype=errortype)

# Signup page
@bp.route('/signup')
def signup():
    return render_template('signup.html')

# New user module. Does not render a template.
@bp.route('/newuser', methods=['POST'])
def newuser():

    result = api.sign_new_user(
        email=request.form['email'],
        password=request.form['password'],
        name=request.form['name']
    )
    
    print("ran new user script")
    print(result)
    return redirect('/signup')
