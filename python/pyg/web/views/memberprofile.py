import os
import datetime

import flask
from wtforms import Form, StringField, TextAreaField, HiddenField, validators
from sqlalchemy import func

from pyg.web import db, models


"""
Member Profile page
Is a view if it's not *your* member profile, otherwise is an editable form that allows you to update your profile information.  This behavior is controlled by the template.

This is the view that links to all the admin things for stuff like teams, fundraisers, etc.

TODO(ben):
- currently, this view shows some arbitrary member if no member is selected (via setting the userid).  This is not something that's likely to ever happen (the user would have to type the URL in manually) but it's weird and pointless and I should change it.
- Couldn't think of any validators for the profile form off the top of my head.
"""

bp = flask.Blueprint("userprofile", __name__)


class MemberProfileForm(Form):
    handle = StringField("Handle")
    location = StringField("Location")
    twitch_handle = StringField("Twitch Handle")
    about = TextAreaField("About")


def update_user_profile(id, name, about, location, twitch_handle, handle):
    """updates Member.  Used primarily in user profile"""
    user = db.web.session.query(models.Member).get(id)
    if not user:
        user = models.Member(
            about=about, location=location, twitch_handle=twitch_handle)
    else:
        user.about = about
        user.location = location
        user.twitch_handle = str(twitch_handle)
        user.handle = handle
    db.web.session.commit()


@bp.route('/profile/<userid>', methods=['GET', 'POST'])
@bp.route('/profile')
def memberprofile(userid=1):
    member = db.web.session.query(models.Member).get(userid)
    auth = member.auth
    fundraisers = db.web.session.query(
        models.Fundraiser).filter(
        models.Fundraiser.active == True,
        models.Fundraiser.member_id == userid)
    form = MemberProfileForm(flask.request.form, member)
    upcoming_fundraiser = None
    past_fundraisers = []
    numplayers = db.web.session.query(func.max(models.Member.rank)).one()[0]
    for i in member.fundraisers:
        try:
            if i.end_date >= datetime.datetime.now(
            ) and i.end_date <= upcoming_fundraiser.end_date and i.active:
                upcoming_fundraiser = i
        except AttributeError:
            upcoming_fundraiser = i

    for i in member.fundraisers:
        if i.end_date <= datetime.datetime.now() and i.active:
            past_fundraisers.append(i)

    if flask.request.method == 'POST' and form.validate():
        update_user_profile(
            flask.session['userid'],
            form.handle.data,
            form.about.data,
            form.location.data,
            form.twitch_handle.data,
            form.handle.data
        )
    return flask.render_template(
        'content_member_profile.html', form=form, member=member, auth=auth, fundraisers=fundraisers, upcoming_fundraiser=upcoming_fundraiser, numplayers=numplayers)
