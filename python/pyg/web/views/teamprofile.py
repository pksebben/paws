import flask

from pyg.web import db, models


"""
Team Profile page
Profile for teams.  Like the Member profile pages, if the logged in user is an owner this should present a form that can be modified in place of any data fields (this should be managed in the template)

TODO(ben): 'update team' view
"""


bp = flask.Blueprint("teamprofile", __name__)


def update_team_profile(id):
    team = db.web.session.query(models.Team).get(id)
    db.web.session.commit()


@bp.route("/teamprofile/<teamid>")
def teamprofile(teamid):
    # TODO: get the currently logged in user and check if it's an owner on
    # this page.
    team = db.web.session.query(models.Team).get(teamid)
    # TODO (ben) : Need to wire up flask.session['userid'] and MemberToTeam.is_owner
    is_owner = db.web.session.query(models.MemberToTeam).filter_by(member_id = flask.session['userid']).one().is_owner
    return flask.render_template("content_teamprofile.html", team=team, is_owner = is_owner)
