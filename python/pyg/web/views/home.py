import flask
from flask import render_template
from sqlalchemy import desc, func

from pyg.web import models, db


"""
Home page
fairly self-explanatory.

TODO:
- do we want to factor out the leaderboard donations function present here?  I believe that it shows up in a couple of other places.  Might be slightly awkward given that there's a leaderboard function here and a leaderboard view, but really no less awkward than doing the same thing just with duplicate code.
"""

bp = flask.Blueprint('home', __name__)


@bp.route('/')
def home():
    donations = db.web.session.query(
        models.Member.handle,
        func.sum(models.Donation.amount).label('total')
    ).join(models.Donation
    ).group_by(
        models.Member.handle).order_by(desc('total')).all()
    leaderboard_players = enumerate(donations, start=1)
    news = db.web.session.query(models.NewsArticle).order_by(
        desc("datetime"))
    return render_template('content_home.html', news=news, leaderboard_players=leaderboard_players)
