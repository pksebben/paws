import flask


"""
Account Deleted page

This just serves a notification that account deletion has been successful.

TODO (ben) : see if there's a way to use __repr__ or some such to implement hiding of deleted records.  Alternatively, there may be some magic in SQLAlchemy
TODO(ian) : Are we using soft deletion?  If not, how do you want to handle data retention?

"""

bp = flask.Blueprint("account_deleted", __name__)


@bp.route('/account_deleted')
def account_deleted():
    return flask.render_template("account_deleted.html")
