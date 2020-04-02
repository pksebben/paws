import datetime

import flask

from pyg.web import db, models


"""
Create Fundraiser route

This does not render a view, rather, it creates a blank fundraiser as a template and reroutes to the 'edit fundraiser' view, to allow the user to actually configure the fundraiser.  This mechanism implements an 'active' field, which gets set to True as soon as the fundraiser is sufficiently configured by the user.

NOTE: This feels hacky.  Perhaps refactor later.
"""

bp = flask.Blueprint("create_fundraiser", __name__)


@bp.route('/createfundraiser', methods=["GET", "POST"])
def create_fundraiser():
    """create a new fundraiser and reroute to the fundraiser page"""
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
    redstring = '/fundraiser/' + str(fundraiser.id)
    return flask.redirect(redstring)
