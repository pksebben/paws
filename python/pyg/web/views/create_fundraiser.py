import datetime

import flask
from wtforms import StringField, DateField, IntegerField, TextAreaField, Form, validators
from wtforms.ext import dateutil
from pyg.web import db, models

bp = flask.Blueprint("create_fundraiser", __name__)


@bp.route('/createfundraiser/<errtype>')
@bp.route('/createfundraiser', methods=["GET", "POST"])
def create_fundraiser(errtype=None):
    """create a new fundraiser and reroute to the fundraiser page"""
    fundraiser = models.Fundraiser(
        name="Name your fundraiser",
        created=datetime.datetime.now(),
        start_date=datetime.datetime.now(),
        end_date=datetime.datetime.now(),
        target_funds=500,
        active=False,
        member_id = flask.session['userid']
    )
    frid = db.web.session.add(fundraiser)
    db.web.session.commit()
    redstring = '/fundraiser/' + str(fundraiser.id)
    return flask.redirect(redstring)
