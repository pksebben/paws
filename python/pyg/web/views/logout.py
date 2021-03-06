import flask


"""
Logout route
Does not render a view, but rather pops user out of session and redirects to home.
TODO (ben) : RTFM for a way to do this routelessly
"""

bp = flask.Blueprint('logout', __name__)

@bp.route('/logout')
def logout():
    flask.session.pop('userid')
    return flask.redirect("/")
