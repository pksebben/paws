import flask
from sqlalchemy import desc

from pyg.web import models, db


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
