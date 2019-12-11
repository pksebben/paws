import flask

bp = flask.Blueprint("teamprofile", __name__)


@bp.route("/teamprofile/<teamid>")
def teamprofile():
    return flask.render_template("content_teamprofile.html")
