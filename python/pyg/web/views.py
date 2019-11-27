import datetime as dt
import sys

import werkzeug.exceptions
import flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from marshmallow import Schema, fields, post_load, ValidationError

from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

import pyg.web
from pyg.web import plugin
from pyg.web import models
from pyg.web import db
from pyg.web import testing
from pyg.web import auth
from pyg.web import api
from pyg.web.exceptions import PasswordError, UserNotFoundError



bp = flask.Blueprint('views', __name__)

# Homepage
@bp.route('/')
def home():
    # TODO: Implement 'user logged in' data
    if 'userid' in session:
        print("user id is")
        print(session['userid'])
        userid = session['userid']
        user=db.web.session.query(models.Person).get(userid)
        username = user.auth.name
        return render_template('content_home.html', username=username)
    else:
        # this is supposed to be a special value that causes pages to behave as they should
        # when no one is logged in.
        return render_template('content_home.html', username=None)


# Gamer profile page. 
@bp.route('/gamerprofile/<gamerid>')
def gamerprofile(gamerid):

    testing.populate() # Testing function

    user = db.web.session.query(models.Person).get(gamerid)
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


# Error page.
@bp.route('/shitsonfireyo/<errortype>')
@bp.route('/shitsonfireyo')
def errorpage(errortype=None):
    return render_template('errorpage.html', errortype=errortype)

# Signup page
@bp.route('/signup/<failtype>')
@bp.route('/signup')
def signup(failtype=None):
    if failtype == None:
        return render_template('signup.html', failure_text="")
    elif failtype == "userexists":
        return render_template('signup.html', failure_text="We found a user with that email.")        

# About page
@bp.route('/about')
def about():
    return render_template('content_about.html')

"""The following modules do not render templates, and are more for accessing parts of the database and performing queries.  They may, however, perform redirects.

We may want to consider putting these in their own blueprint, to differentiate."""

@bp.route('/shelterprofile')
def shelterprofile():
    return render_template('content_shelterprofile.html')



# New user module. Does not render a template.
@bp.route('/newuser', methods=['POST'])
def newuser():

    try:
        api.sign_new_user(
            email=request.form['email'],
            password=request.form['password'],
            name=request.form['name']
        )
    except IntegrityError as err:
        print(err)
        return redirect('/signup/userexists')
    
    return redirect('/')

# authorization module.  Does not render a template, but redirects to login or homepage based on failure or success
@bp.route('/authorize', methods=['POST'])
def authorize():
    try:
        auth.user(email = request.form['email'], password=request.form['password'])
        return redirect('/')
    except PasswordError as err:
        print(err)
        return redirect('/login/passworderr')
    except UserNotFoundError as err:
        print(err)
        return redirect('/login/usererr')
            
