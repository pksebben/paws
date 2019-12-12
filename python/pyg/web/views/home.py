import flask
from flask import render_template
from sqlalchemy import desc

from pyg.web import models, db

bp = flask.Blueprint('home', __name__)


@bp.route('/')
def home():
    news = db.web.session.query(models.NewsArticle).order_by(
        desc("datetime"))
    return render_template('content_home.html', news=news)
