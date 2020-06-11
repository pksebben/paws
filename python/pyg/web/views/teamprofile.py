"""
Team Profile page
Profile for teams.  Like the Member profile pages, if the logged in user is an owner this should present a form that can be modified in place of any data fields (this should be managed in the template)

TODO(ben) : Wire members to teams
TODO(ben): Add member function
TODO(ben): 'update team' view
TODO(ben): wire together donation data, campaign data
TODO(ian): How are donations tied to teams? esp. now that we have tiltify.
"""

import flask

from pyg.web import db, models


bp = flask.Blueprint("teamprofile", __name__)


def update_team_profile(id):
    team = db.web.session.query(models.Team).get(id)
    db.web.session.commit()


@bp.route("/teamprofile/<teamid>")
def teamprofile(teamid):
    """serve up the team profile page"""
    team = db.web.session.query(models.Team).get(teamid)
    if flask.session.get('userid'):
        user_id = flask.session.get('userid')
        print("TEAM DOT MEMBER?")
        print(team.members)
        if user_id in team.member_ids:
            print("User is a member")
            is_member = True
            is_owner = team.members[user_id].is_owner
        else:
            print("user is not a member")
            is_member = False
            is_owner = False
    else:
        is_owner = False
    return flask.render_template("content_teamprofile.html", team=team, is_owner=is_owner, is_member=is_member)
