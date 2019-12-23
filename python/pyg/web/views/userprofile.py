import flask

from wtforms import Form, StringField, TextAreaField, HiddenField, validators
from pyg.web import db, models

bp = flask.Blueprint("userprofile", __name__)


class UserProfileForm(Form):
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
def userprofile(userid=1):
    member = db.web.session.query(models.Member).get(userid)
    auth = member.auth
    fundraisers = member.fundraisers
    form = UserProfileForm(flask.request.form, member)
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
        'content_gamer_profile.html', form=form, member=member, auth=auth, fundraisers=fundraisers)
