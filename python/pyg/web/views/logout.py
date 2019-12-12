import flask

bp = flask.Blueprint('logout', __name__)

@bp.route('/logout')
def logout():
    flask.session.pop('userid')
    return flask.redirect("/")
