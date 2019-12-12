import flask

bp =flask.Blueprint('leaderboard', __name__)

@bp.route('/leaderboard')
def leaderboard():
    return flask.render_template('content_leaderboard.html')
