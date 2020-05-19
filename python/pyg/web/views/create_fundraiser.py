import datetime

import flask
from wtforms import Form, StringField, TextAreaField, validators, SubmitField
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired

from pyg.web import db, models



"""
Create Fundraiser route

This does not render a view, rather, it creates a blank fundraiser as a template and reroutes to the 'edit fundraiser' view, to allow the user to actually configure the fundraiser.  This mechanism implements an 'active' field, which gets set to True as soon as the fundraiser is sufficiently configured by the user.

TODO (ben) : for some reason, this module allows dupe names, which should be impossible.  Investigate.
++++ also, the dupe validator apparently does nothing.
"""

bp = flask.Blueprint("create_fundraiser", __name__)

# custom validator
def daterange(soonest, latest):
    msg = "Must be no sooner than %s and no later than %s" % (soonest, latest)

    def _daterange(form, field):
        date = field.data
        if date < soonest or date > latest:
            raise ValidationError(msg)
    return _daterange

def uniquename():
    msg = "We found a fundraiser with that name already."
   
    def _uniquename(form, field):
        name = field.data
        if name in db.web.session.query(models.Fundraiser.name).all():
            raise ValidationError(msg)
    return _uniquename

# WTForm
class FundraiserForm(Form):
    """fundraiser input form"""
    date_constraint = daterange(datetime.date.today(),
                                datetime.date.max)
    unique_constraint = uniquename()
    name = StringField("Name", validators=[InputRequired(), Length(max=25), unique_constraint])
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
    about = TextAreaField("Write an About section")
    submit = SubmitField("submit fundraiser")


@bp.route('/createfundraiser', methods=["GET", "POST"])
def create_fundraiser():
    """create a new fundraiser and reroute to the fundraiser page"""
    form = FundraiserForm(flask.request.form)
    if flask.request.method == 'POST' and form.validate:
        fundraiser = models.Fundraiser(
            name=form.name.data,
            created=datetime.datetime.now(),
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            target_funds=form.target_funds.data,
            member_id=flask.session['userid']
        )
        frid = db.web.session.add(fundraiser)
        db.web.session.commit()
        return flask.redirect('fundraiser/' + str(fundraiser.id))
    else:
        return flask.render_template("content_create_fundraiser.html", form=form)
