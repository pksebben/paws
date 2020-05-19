import flask
from sqlalchemy import desc
from wtforms import Form, StringField

from pyg.web import models, db


"""
News Page

Articles are managed using the admin module, accessible via the /admin/ route.

WARNING: this page uses a different routing method from most of the other pages, implementing a 'route prefix'.  This is defined when the blueprint is registered in app.py.  If you cannot find this page, look there first.

TODO (ben) : There should be some form of navigation / search on the news page.  
"""

# TODO | ian : do we wanna axe this section?  Will there be news?

bp = flask.Blueprint('news', __name__)

class SearchForm(Form):
    searchstring = StringField("Search for articles")


@bp.route('/', defaults={'slug': None})
@bp.route('/<slug>', methods=['GET', 'POST'])
def article(slug=None):
    form = SearchForm(flask.request.form)
    toc = db.web.session.query(models.NewsArticle.slug,
                               models.NewsArticle.headline, models.NewsArticle.date)
    articles = db.web.session.query(models.NewsArticle).order_by(
        desc("date"))
    if slug:
        articles = articles.filter_by(slug=slug)
    return flask.render_template(
        'content_news.html', toc=toc, articles=articles, form=form)
