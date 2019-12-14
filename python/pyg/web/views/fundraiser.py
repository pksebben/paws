import re
from marshmallow import Schema, fields, ValidationError
###############

import flask
import datetime

from pyg.web import db, models


class FundraiserSchema(Schema):
    name = fields.String(required=True)
    """this next field might need to be extended via the _serialize method."""
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    target_funds = fields.Integer(required=True)
    about = fields.String(required=True)
    member_id = fields.Integer(required=True)
    created = fields.DateTime(required=True, default=datetime.datetime.now())
    




bp = flask.Blueprint("fundraiser", __name__)

@bp.route("/fundraiser/<frid>")
@bp.route("/fundraiser", methods=['GET', 'POST'])
def fundraiser(frid=None):
    if frid:
        fundraiser = db.web.session.query(models.Fundraiser).get(frid)
        return flask.render_template("content_fundraiser.html", fundraiser=fundraiser)
    else:
        if flask.request.method == 'POST':
            fraiser = models.Fundraiser(
                name = flask.request.form['name'],
                start_date = datetime.datetime.now(),
                target_funds = flask.request.form['target_funds'],
                about = flask.request.form['about'],
                member_id = flask.request.form['userid'],
                created = datetime.datetime.now(),
                end_date = datetime.datetime.now()
            )
            frid = db.web.session.add(fraiser)
            db.web.session.commit()
            fundraiser = db.web.session.query(models.Fundraiser).get(frid)
            return flask.render_template("content_fundraiser.html", fundraiser=fundraiser)
        else:
            fundraisers = db.web.session.query(models.Fundraiser).all()
            return flask.render_template("content_fundraiser.html", fundraisers=fundraisers)
