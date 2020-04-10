import datetime

import flask
from wtforms import Form, StringField, TextAreaField, validators
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired

from pyg.web import db, models



"""
Create Fundraiser route

This does not render a view, rather, it creates a blank fundraiser as a template and reroutes to the 'edit fundraiser' view, to allow the user to actually configure the fundraiser.  This mechanism implements an 'active' field, which gets set to True as soon as the fundraiser is sufficiently configured by the user.

NOTE: This feels hacky.  Perhaps refactor later.

TODO (ben) : Rework this whole thingerdoodle.  See below
---------------
So this shortcut is going to end up massacring the database with a flood of bullshit.  It's an antipattern.
What needs to happen is the following:
 1 - clone the fundraiser page and work it as an input for new fundraisers
 2 - this view should direct there.  
 3 - if the fundraiser is not properly validated, it does not touch the db.  full stop.
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


# WTForm
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
    about = TextAreaField("Write an About section")



@bp.route('/createfundraiser', methods=["GET", "POST"])
def create_fundraiser():
    """create a new fundraiser and reroute to the fundraiser page"""
    form = FundraiserForm()
    fundraiser = models.Fundraiser(
        name="Name your fundraiser",
        created=datetime.datetime.now(),
        start_date=datetime.datetime.now(),
        end_date=datetime.datetime.now(),
        target_funds=500,
        active=False,
        member_id=flask.session['userid']
    )
    frid = db.web.session.add(fundraiser)
    db.web.session.commit()
    return flask.render_template("content_create_fundraiser.html", form=form)
