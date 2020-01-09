import flask


"""
This is the page to sign up new partners such as shelters and marketing partners.

TODO:
basically everything, starting with a coherent UX design around the partnering process.  May want to involve clock in this.

"""

bp = flask.Blueprint('partnering', __name__)

@bp.route('/partnering')
def partering():
    return flask.render_template('partnering.html')
