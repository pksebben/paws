import flask


"""
About page

Fairly self-explanatory.  All content is loaded from the db, and is managed using the admin panel, accessible in the /admin route.

TODO(clock): What is going to be in here?

TODO(ben):
-make models for whatever data goes here
-styling
-grab/serve that data
-create html
"""

bp = flask.Blueprint('about', __name__)


@bp.route('/about')
def aboutpage():
    return flask.render_template('content_about.html')
