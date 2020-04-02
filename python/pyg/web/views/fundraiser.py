import datetime

import flask
from wtforms import Form, StringField, TextAreaField, validators
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired

from pyg.web import db, models


"""
Fundraiser page

This is both the view to look at a fundraiser (if you're not an owner) and the view to edit fundraisers (if you are.)  Newly created fundraisers are modified here before going live by setting the 'active' bit.

Whether the fundraiser is displayed in 'edit' or 'view' mode is controlled in the template.

Note on forms: WTForms has this great feature that will take an object and attempt to assume default values for fields based on matching the data in that object to the names of the fields. This is done here, and any changes to the fundraiser model or the fundraiser form must be reflected in the other.

TODO(ben): (maybe, see create_fundraiser NOTE)Implement 'hiding' behavior for inactive fundraisers.
"""


def daterange(soonest, latest):
    msg = "Must be no sooner than %s and no later than %s" % (soonest, latest)

    def _daterange(form, field):
        date = field.data
        if date < soonest or date > latest:
            raise ValidationError(msg)
    return _daterange


class FundraiserForm(Form):
    date_constraint = daterange(datetime.date.today(),
                                datetime.date.max)
    name = StringField("Name", validators=[InputRequired(), Length(max=25)])
    end_date = DateField(
        "End Date",
        validators=[
            DataRequired(),
            date_constraint])
    start_date = DateField(
        "Start Date",
        validators=[
            DataRequired(),
            date_constraint
        ])
    target_funds = IntegerField("Target Funds", validators=[DataRequired()])
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

    TODO (ben) : make the list of fundraisers searchable
    TODO (ben) : update the template to show 'about' section
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
            fundraiser.active = True
            db.web.session.commit()
        return flask.render_template(
            "content_fundraiser.html", fundraiser=fundraiser, form=form)

    else:

        fundraisers = db.web.session.query(models.Fundraiser).all()
        return flask.render_template(
            "content_fundraiser.html", fundraisers=fundraisers)
