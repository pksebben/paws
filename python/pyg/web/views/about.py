import flask

bp = flask.Blueprint('about', __name__)


@bp.route('/about')
def aboutpage():
    return flask.render_template('content_about.html')
