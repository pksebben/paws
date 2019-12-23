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


@bp.route("/fundraiser/<frid>", methods=['GET', 'POST'])
@bp.route("/fundraiser", methods=['GET', 'POST'])
def fundraiser(frid=None):
    """
    Fundraiser Page.
    If fundraiser is owned by the currently logged in user, view the fundraiser in
    'edit mode' - this behavior is controlled in the template.

    If no fundraiser is selected to view (via fundraiser ID), show a list of all fundraisers.

    TODO
    make the list of fundraisers searchable


    """
    if frid:
        fundraiser = db.web.session.query(models.Fundraiser).get(frid)
        form = FundraiserForm(flask.request.form, fundraiser)
        if flask.request.method == "POST":
            fundraiser.name = form.name.data
            fundraiser.end_date = form.end_date.data
            fundraiser.start_date = form.start_date.data
            fundraiser.target_funds = form.target_funds.data
            fundraiser.about = form.about.data
            db.web.session.commit()
        # form.name.data = fundraiser.name
        # form.end_date = fundraiser.end_date
        return flask.render_template(
            "content_fundraiser.html", fundraiser=fundraiser, form=form)

    else:

        fundraisers = db.web.session.query(models.Fundraiser).all()
        return flask.render_template(
            "content_fundraiser.html", fundraisers=fundraisers)
