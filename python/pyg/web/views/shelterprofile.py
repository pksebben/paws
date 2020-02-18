import flask

from pyg.web import db, models

bp = flask.Blueprint("shelterprofile", __name__)


@bp.route("/shelter/<shelterid>")
def shelterprofile(shelterid):
    shelter = db.web.session.query(models.Shelter).get(shelterid)
    return flask.render_template(
        "content_shelterprofile.html", shelter=shelter)
