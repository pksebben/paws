import flask


"""
Account Deleted page

This just serves a notification that account deletion has been successful.

#ON HOLD#
until deletion mechanics are better fleshed out.

TODO:
Are there further instructions that we want to implement?
Should there be a timed redirect here?
"""

bp = flask.Blueprint("account_deleted", __name__)

@bp.route('/account_deleted')
def account_deleted():
    return flask.render_template("account_deleted.html")
