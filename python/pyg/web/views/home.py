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



@bp.route('/', methods=["GET", "POST"])
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
                           leaderboard_players=leaderboard_players)
