import flask

from pyg.web import db, models

bp = flask.Blueprint("fundraiser", __name__)

@bp.route("/fundraiser/<frid>")
@bp.route("/fundraiser")
def fundraiser(frid=None):
    if frid:
        fundraiser = db.web.session.query(models.Fundraiser).get(frid)
        return flask.render_template("content_fundraiser.html", fundraiser=fundraiser)
    else:
        fundraisers = db.web.session.query(models.Fundraiser).all()
        return flask.render_template("content_fundraiser.html", fundraisers=fundraisers)
