import re
from marshmallow import Schema, fields, ValidationError
from wtforms import Form, StringField, IntegerField, DateTimeField, DateField, TextAreaField, validators
###############

import flask
import datetime

from pyg.web import db, models

"""TODO: finish"""


class FundraiserForm(Form):
    name = StringField("Name")
    end_date = DateField("End Date")
    target_funds = IntegerField("Target Funds")
    about = TextAreaField("About")


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
        return flask.render_template(
            "content_fundraiser.html", fundraiser=fundraiser)
    else:
        if flask.request.method == 'POST':
            fraiser = models.Fundraiser(
                name=flask.request.form['name'],
                start_date=datetime.datetime.now(),
                target_funds=flask.request.form['target_funds'],
                about=flask.request.form['about'],
                member_id=int(flask.request.form['userid']),
                created=datetime.datetime.now(),
                end_date=datetime.datetime.now()
            )
            schema = FundraiserSchema()
            dumped = schema.dump(fraiser)
            errors = FundraiserSchema().validate(data={
                "name": fraiser.name,
                "start_date": str(fraiser.start_date),
                "end_date": str(fraiser.end_date),
                "target_funds": fraiser.target_funds,
                "about": fraiser.about,
                "member_id": fraiser.member_id,
                "created": str(fraiser.created)
            })
            print(fraiser.__dict__)
            print(errors)
            frid = db.web.session.add(fraiser)
            try:
                db.web.session.commit()
                print(frid)
                fundraiser = db.web.session.query(models.Fundraiser).get(frid)
                return flask.render_template(
                    "content_fundraiser.html", fundraiser=fundraiser)
            except Exception as err:
                # TODO: Create a pattern for form validation sitewide
                # may use WTForms
                # may use marshmallow and raw flask.
                raise err
            # except ValidationError as err:
            #     # TODO: what happens on validation errors?
            #     pass
            # except IntegrityError as err:
            #     return flask.redirect("/createfundraiser")
        else:
            fundraisers = db.web.session.query(models.Fundraiser).all()
            return flask.render_template(
                "content_fundraiser.html", fundraisers=fundraisers)
