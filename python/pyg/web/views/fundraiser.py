import datetime

import flask
from wtforms import Form, StringField, IntegerField, DateTimeField, DateField, TextAreaField, validators

from pyg.web import db, models


class FundraiserForm(Form):
    name = StringField("Name")
    end_date = DateField("End Date")
    start_date = DateField("Start Date")
    target_funds = IntegerField("Target Funds")
    about = TextAreaField("About")


bp = flask.Blueprint("fundraiser", __name__)


def new_fundraiser(name, target_funds, about, member_id, end_date):
    fraiser = models.Fundraiser(
        name=name,
        start_date=datetime.datetime.now(),
        target_funds=target_funds,
        about=about,
        member_id=int(member_id),
        created=datetime.datetime.now(),
        end_date=end_date
    )

    frid = db.web.session.add(fraiser)


@bp.route("/fundraiser/<frid>")
@bp.route("/fundraiser", methods=['GET', 'POST'])
def fundraiser(frid=None):
    form = FundraiserForm(flask.request.form)
    if frid:
        fundraiser = db.web.session.query(models.Fundraiser).get(frid)
        return flask.render_template(
            "content_fundraiser.html", fundraiser=fundraiser, form=form)





    
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
