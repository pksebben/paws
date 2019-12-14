import flask

bp = flask.Blueprint("create_fundraiser", __name__)

@bp.route('/createfundraiser')
def create_fundraiser():
    return flask.render_template("content_fundraiser_create.html")
