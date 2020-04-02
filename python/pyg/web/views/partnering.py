import flask


"""
This is the page to sign up new partners such as shelters and marketing partners.

TODO (ben) : Make a page and think more on what it needs

"""

bp = flask.Blueprint('partnering', __name__)

@bp.route('/partnering')
def partering():
    return flask.render_template('partnering.html')
