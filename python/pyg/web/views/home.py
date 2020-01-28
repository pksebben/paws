import flask
from flask import render_template
from sqlalchemy import desc, func

from pyg.web import models, db
from pyg.web.views.login import LoginForm


"""
Home page
fairly self-explanatory.

TODO:
- Implement windowing for the leaderboard query
- find a home for the leaderboard windowing function so it becomes useful for member profile pages, the homepage, team profiles, and fundraisers.
"""

bp = flask.Blueprint('home', __name__)

def rankedlist():
    donations = db.web.session.query(
        models.Member.handle,
        func.sum(models.Donation.amount).label('total')
    ).join(models.Donation
    ).group_by(
        models.Member.handle).order_by(desc('total')).all()
    leaderboard_players = enumerate(donations, start=1)
    return leaderboard_players

@bp.route('/')
def home():
    loginform = LoginForm(flask.request.form)
    donations = db.web.session.query(
        models.Member.handle, models.Member.id,
        func.sum(models.Donation.amount).label('total')
    ).join(models.Donation
    ).group_by(
        models.Member.handle).order_by(desc('total')).all()
    leaderboard_players = enumerate(donations, start=1)
    news = db.web.session.query(models.NewsArticle).order_by(
        desc("date"))
    return render_template('content_home.html', news=news, leaderboard_players=leaderboard_players, loginform=loginform)
