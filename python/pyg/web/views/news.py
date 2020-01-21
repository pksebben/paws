import flask
from sqlalchemy import desc

from pyg.web import models, db


"""
News Page

Articles are managed using the admin module, accessible via the /admin/ route.

WARNING: this page uses a different routing method from most of the other pages, implementing a 'route prefix'.  This is defined when the blueprint is registered in app.py.  If you cannot find this page, look there first.
"""
bp = flask.Blueprint('news', __name__)


@bp.route('/', defaults={'slug': None})
@bp.route('/<slug>')
def article(slug=None):
    toc = db.web.session.query(models.NewsArticle.slug,
                               models.NewsArticle.headline)
    articles = db.web.session.query(models.NewsArticle).order_by(
        desc("datetime"))
    if slug:
        articles = articles.filter_by(slug=slug)
    return flask.render_template(
        'content_news.html', toc=toc, articles=articles)
