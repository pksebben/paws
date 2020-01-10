import flask

from pyg.web import db, models


"""
Team Profile page
Profile for teams.  Like the Member profile pages, if the logged in user is an owner this should present a form that can be modified in place of any data fields (this should be managed in the template)

TODO:
- It looks like the update team profile function is, well, not functional.  
- Probably everything.  This is way too barebones to be nearly complete.
"""


bp = flask.Blueprint("teamprofile", __name__)


def update_team_profile(id):
    team = db.web.session.query(models.Team).get(id)
    db.web.session.commit()

@bp.route("/teamprofile/<teamid>")
def teamprofile():
    # TODO: get the currently logged in user and check if it's an owner on this page.
    return flask.render_template("content_teamprofile.html")
