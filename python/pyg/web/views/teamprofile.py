import flask

from pyg.web import db, models

bp = flask.Blueprint("teamprofile", __name__)


def update_team_profile(id):
    team = db.web.session.query(models.Team).get(id)
    db.web.session.commit()

@bp.route("/teamprofile/<teamid>")
def teamprofile():
    # get the currently logged in user and check if it's an owner on this page.
    return flask.render_template("content_teamprofile.html")
