import flask
from flask import render_template
from sqlalchemy import desc, func

from pyg.web import models, db

bp = flask.Blueprint('home', __name__)


@bp.route('/')
def home():
    donations = db.web.session.query(
        models.Profile.handle,
        func.sum(models.Donation.amount).label('total')
    ).join(models.Member.profile
    ).join(models.Donation
    ).group_by(
        models.Profile.handle).order_by(desc('total')).all()
    leaderboard_players = enumerate(donations, start=1)
    news = db.web.session.query(models.NewsArticle).order_by(
        desc("datetime"))
    return render_template('content_home.html', news=news, leaderboard_players=leaderboard_players)
