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


@bp.route('/login/<failtype>')
@bp.route('/login')
def login(failtype=None):
    testing.populate()
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


    # REFACTORING HERE
    auth_code = auth.user(email = request.form['email'], password=request.form['password'])

    print("auth code: ", auth_code)
    
    if auth_code == "auth_success":

        return redirect('/')
        # # TODO: replace this next block with something better, perhaps return the user id in the auth module
        # userauth = db.web.session.query(models.UserAuth).filter_by(email=email)
        # q = list(userauth)        
        # session['userid'] = q[0].id
    elif auth_code == "auth_pass_err":
        return redirect('/login/passworderr')
    elif auth_code == "auth_email_err":
        return redirect('/login/usererr')
    else:
        # TODO: implement proper handler for bad auth code
        print("Bad auth code. TODO: implement proper error handler")
        return redirect('/shitsonfireyo')

@bp.route('/shitsonfireyo/<errortype>')
@bp.route('/shitsonfireyo')
def errorpage(errortype=None):
    return render_template('errorpage.html', errortype=errortype)
