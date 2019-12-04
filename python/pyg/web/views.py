import datetime as dt

import werkzeug.exceptions
import flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect

from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

import pyg.web
from pyg.web import auth
from pyg.web import models
from pyg.web import db
from pyg.web import testing


def sign_new_user(email, password, name):

    newperson = models.Person(created=dt.datetime.now())
    newperson.auth = models.UserAuth(name=name, password=password, email=email)
    db.web.session.add(newperson)
    db.web.session.commit()
    # change to structlog
    # print("user created")
    

def update_user_profile(id, about, birthday, location):
    user = db.web.session.query(models.Person).get(id)
    if not user.profile:
        user.profile = models.UserProfile(about=about, birthday=birthday, location=location)
        # change to structlog
        # print('added user profile')
    else:
        user.profile.about = about
        user.profile.birthday = birthday
        user.profile.location = location
        # change to structlog
        # print('updated user profile')
    db.web.session.commit()
    # change to structlog
    # print("user updated")


bp = flask.Blueprint('views', __name__)

# Homepage
@bp.route('/')
def home():
    # TODO: Implement 'user logged in' data
    if 'userid' in session:
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
@bp.route('/gamerprofile')
def gamerprofile(gamerid=None):

    testing.populate() # Testing function

    if not gamerid:
        gamerid = session['userid']
    user = db.web.session.query(models.Person).get(gamerid)
    auth = user.auth
    profile = user.profile

    # is passing auth as a parameter a security liability?
    return render_template('content_gamer_profile.html', auth=auth, profile=profile)


@bp.route('/editprofile')
def editprofile():

    user = db.web.session.query(models.Person).get(session['userid'])
    auth = user.auth
    profile = user.profile

    return render_template('edit_gamerprofile.html', auth=auth, profile=profile)


def authorize():
    try:
        auth.user(email = request.form['email'], password=request.form['password'])
        return redirect('/')
    except auth.AuthError as err:
        # change to structlog
        print(err)
        return render_template('login.html', )

    
# login page.  Might become a modal later.  Gotta figure out how to do modals.
@bp.route('/login', methods=['POST'])
@bp.route('/login')
def login(failtype=None):
    # WIP - implement flask-login here
    # if request.method == 'POST':
    #     try:
    #         auth.user(email = request.form['email'], password=request.form['password'])
    #         return redirect('/')
    #     except PasswordError as err:
    #         return render_template('')
    if request.method == 'POST':
        try:
            auth.user(email = request.form['email'], password = request.form['password'])
            return redirect('/')
        except AuthError:
            # TODO: should implement some flask flashing here.  Revisit.
            return render_template('login.html', failure_text="invalid credentials. Please try again.")
    else:
        return render_template('login.html', failure_text="")

    

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

# Shelter profile page
@bp.route('/shelterprofile')
def shelterprofile():
    return render_template('content_shelterprofile.html')


"""The following modules do not render templates, and are more for accessing parts of the database and performing queries.  They may, however, perform redirects.

We may want to consider putting these in their own blueprint, to differentiate."""

# Testing purposes. 
@bp.route('/logout')
def logout():
    # change to structlog
    print('logging out')
    session.pop('userid', None)
    return redirect('/')


 # TODO: sanity check this module
@bp.route('/submit-user-edit', methods=["POST"])
def submit_user_edit():
    # change to structlog
    print(request.form)
    user = db.web.session.query(models.Person).get(session['userid'])
    user.auth.name = request.form['username']
    user.profile.location = request.form['location']
    user.profile.about = request.form['about']
    db.web.session.commit()    
    return redirect('/gamerprofile')
    

# New user module. Does not render a template.
@bp.route('/newuser', methods=['POST'])
def newuser():

    try:
        sign_new_user(
            email=request.form['email'],
            password=request.form['password'],
            name=request.form['name']
        )
    except IntegrityError as err:
        # change to structlog
        print(err)
        return redirect('/signup/userexists')
    
    return redirect('/')



# Leaderboard.  Might be turned into an imported module
@bp.route('/leaderboard')
def leaderboard():
    return render_template('content_leaderboard.html')
