import flask


"""
About page

Fairly self-explanatory.  All content is loaded from the db, and is managed using the admin panel, accessible in the /admin route.
"""

bp = flask.Blueprint('about', __name__)


@bp.route('/about')
def aboutpage():
    return flask.render_template('content_about.html')
