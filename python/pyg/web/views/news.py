import flask
from sqlalchemy import desc

from pyg.web import models, db

bp = flask.Blueprint('news', __name__)

"""
Qs:
How are we going to serve up the news?  What does the end result look like?
"""


def retrievenews(newsid):
    return db.web.session.query(models.NewsArticle).get(newsid)


def latestnews():
    n = db.web.session.query(
        models.NewsArticle).order_by(
        desc("datetime")).limit(1).first()
    return n.id


@bp.route('/news')
def newspage():
    artid = latestnews()
    return flask.render_template(
        'content_news.html', article=retrievenews(artid))
