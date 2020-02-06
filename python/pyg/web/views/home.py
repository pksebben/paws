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


@bp.route('/')
def home():
    if flask.session.get('userid'):
        leaderboard_players = rankedlist(member = db.web.session.query(models.Member).get(flask.session['userid']))
    else:
        leaderboard_players = rankedlist(member = db.web.session.query(models.Member).filter_by(rank = 3).first())
    loginform = LoginForm(flask.request.form)
    news = db.web.session.query(models.NewsArticle).order_by(
        desc("date"))
    return render_template('content_home.html', news=news, leaderboard_players=leaderboard_players, loginform=loginform)
