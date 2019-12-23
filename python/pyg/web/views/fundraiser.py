import datetime

import flask
from wtforms import Form, StringField, TextAreaField, validators
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError

from pyg.web import db, models


def daterange(soonest, latest):
    msg = "Must be no sooner than %s and no later than %s" % (soonest, latest)

    def _daterange(form, field):
        date = field.data
        if date < soonest or date > latest:
            raise ValidationError(msg)
    return _daterange


class FundraiserForm(Form):
    """
    TODO
    decide a reasonable max length for names
    update date validators to reflect desired ranges
    """
    name = StringField("Name", validators=[InputRequired(), Length(max=25)])
    end_date = DateField(
        "End Date",
        validators=[
            InputRequired(),
            daterange(
                datetime.date.today(),
                datetime.date(
                    year=2050,
                    month=1,
                    day=1))])
    start_date = DateField("Start Date")
    target_funds = IntegerField("Target Funds")
    about = TextAreaField("About")


bp = flask.Blueprint("fundraiser", __name__)


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
    update the template to show 'about' section
    """
    
    if frid:
        fundraiser = db.web.session.query(models.Fundraiser).get(frid)
        form = FundraiserForm(flask.request.form, fundraiser)
        if flask.request.method == "POST" and form.validate():
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
