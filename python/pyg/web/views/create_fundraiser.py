import flask

bp = flask.Blueprint("create_fundraiser", __name__)

@bp.route('/createfundraiser/<errtype>')
@bp.route('/createfundraiser')
def create_fundraiser(errtype):
    if errtype == "duplicate_name":
        msg = "We found a fundraiser with that name already.  Try renaming your fundraiser."
    else if errtype == "validation_err":
        
    return flask.render_template("content_fundraiser_create.html")
