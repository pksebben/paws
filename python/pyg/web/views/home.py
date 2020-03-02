import random
import datetime

import flask
from flask import render_template
from sqlalchemy import desc, func

from pyg.web import models, db
from pyg.web.views.login import LoginForm, login_user
from pyg.web.views.leaderboard import rankedlist


"""
Home page
fairly self-explanatory.

"""

bp = flask.Blueprint('home', __name__)


"""
Feature section
This is meant to feature a fundraiser or player or team that has been exceptional for some reason or another lately.  Reasons can be:
 - new and active
 - mvp in a particular category
 - trending (in the case of fundraisers)
"""


# //features an active fundraiser
def feature_fundraiser():
    fundraiser = db.web.session.query(
        models.Fundraiser).filter(
        models.Fundraiser.start_date <= datetime.datetime.now(),
        models.Fundraiser.end_date >= datetime.datetime.today()).order_by(
            func.random()).first()
    feature = {
        "type": "fundraiser",
        "name": fundraiser.name,
        "started": fundraiser.start_date,
        "ends": fundraiser.end_date,
        "raised": "IMPLEMENT ME"
    }
    return feature


"""
INCOMPLETE
def feature_team():
    team = db.web.session.query(
        models.Team
    ).filter(func.max(models.Team.date_joined)).first()
    feature = {
        "type": "team",
        "name": team.name,
        "members": "IMPLEMENT"
    }

# feature a streamer

def feature_streamer():
    streamer = db.web.session.query(models.Member)
    feature = {
        "type": "streamer",
        "name": "IMPLEMENT",
        "rank": "IMPLEMENT",
        "raised": "IMPLEMENT",
        "joined": "IMPLEMENT"
    }
"""



@bp.route('/', methods=["GET","POST"])
def home():
    if flask.request.method == "POST" and loginform.validate():
        flask.flash("it's working!")
    loginform = LoginForm(flask.request.form)
    if flask.session.get('userid'):
        leaderboard_players = rankedlist(
            member=db.web.session.query(
                models.Member).get(
                flask.session['userid']))
        member = db.web.session.query(
            models.Member).get(
            flask.session.get('userid'))
    else:
        leaderboard_players = rankedlist(
            member=db.web.session.query(
                models.Member).filter_by(
                rank=3).first())
        member = None
    news = db.web.session.query(models.NewsArticle).order_by(
        desc("date"))
    return render_template('content_home.html', news=news, member=member,
                           leaderboard_players=leaderboard_players, feature=feature_fundraiser())
