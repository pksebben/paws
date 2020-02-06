import random
import datetime

import flask
from flask import render_template
from sqlalchemy import desc, func

from pyg.web import models, db
from pyg.web.views.login import LoginForm
from pyg.web.views.leaderboard import rankedlist


"""
Home page
fairly self-explanatory.

TODO:
- Implement windowing for the leaderboard query
- find a home for the leaderboard windowing function so it becomes useful for member profile pages, the homepage, team profiles, and fundraisers.
"""

bp = flask.Blueprint('home', __name__)


"""
Feature section
This is meant to feature a fundraiser or player or team that has been exceptional for some reason or another lately.  Reasons can be:
 - new and active
 - mvp in a particular category
 - trending (in the case of fundraisers)
"""


# def feature_mvp():
#     team = random.choice(db.web.session.query(models.Team).all())

# def feature_fundraiser():
#     fundraiser = random.choice(db.web.session.query(models.Fundraiser).filter_by(active=True, end_date <= datetime.datetime.now()))
# def pick_feature():


@bp.route('/')
def home():
    if flask.session.get('userid'):
        leaderboard_players = rankedlist(
            member=db.web.session.query(
                models.Member).get(
                flask.session['userid']))
    else:
        leaderboard_players = rankedlist(
            member=db.web.session.query(
                models.Member).filter_by(
                rank=3).first())
    loginform = LoginForm(flask.request.form)
    news = db.web.session.query(models.NewsArticle).order_by(
        desc("date"))
    return render_template('content_home.html', news=news,
                           leaderboard_players=leaderboard_players, loginform=loginform)
