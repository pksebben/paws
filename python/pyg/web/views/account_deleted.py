import flask


"""
Account Deleted page

This just serves a notification that account deletion has been successful.

#ON HOLD#
until deletion mechanics are better fleshed out.

TODO:
- figure out deletion mechanics
 -- Active bit on models
 -- Deactivate accounts on deletion
 -- Accounts should not be displayed (or visible) once made inactive
  --- Profile view
  --- leaderboards
  --- membership on teams
"""

bp = flask.Blueprint("account_deleted", __name__)

@bp.route('/account_deleted')
def account_deleted():
    return flask.render_template("account_deleted.html")
