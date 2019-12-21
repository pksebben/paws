import flask

bp = flask.Blueprint("create_fundraiser", __name__)
# TODO: Is this better accomplished by creating an empty fundraiser and going to the edit fundraiser page?  
@bp.route('/createfundraiser/<errtype>')
@bp.route('/createfundraiser')
def create_fundraiser(errtype):
    if errtype == "duplicate_name":
        msg = "We found a fundraiser with that name already.  Try renaming your fundraiser."
    elif errtype == "validation_err":
        pass
    return flask.render_template("content_fundraiser_create.html")
