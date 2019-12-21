import flask

from wtforms import Form, StringField, TextAreaField, HiddenField, validators
from pyg.web import db, models

bp = flask.Blueprint("userprofile", __name__)

class UserProfileForm(Form):
    handle = StringField("Handle")
    location = StringField("Location")
    twitch_handle = StringField("Twitch Handle")
    about = TextAreaField("About")

def update_user_profile(id, name, about, location, twitch_handle):
    """updates Member.  Used primarily in user profile"""
    user = db.web.session.query(models.Member).get(id)
    if not user:
        user = models.Member(
            about=about, location=location, twitch_handle=twitch_handle)
    else:
        user.about = about
        user.location = location
        user.twitch_handle = str(twitch_handle)
    db.web.session.commit()


@bp.route('/profile/<userid>', methods=['GET', 'POST'])
@bp.route('/profile')
def userprofile(userid=1):
    form = UserProfileForm(flask.request.form)
    try:
        user = db.web.session.query(models.Member).get(userid)
        auth = user.auth
        profile = user
        fundraisers = user.fundraisers
        if flask.request.method == 'get':
            form.handle.data = user.handle
            form.location.data = user.location
            form.twitch_handle.data = user.twitch_handle
            form.about.data = user.about
    except AttributeError as err:
        # how are we going to handle bad values for userid?
        # we want to avoid rendering the page, for sure.
        # we want something logged
        raise err
    if flask.request.method == 'POST':
        update_user_profile(
            flask.session['userid'],
            form.handle.data,
            form.about.data,
            form.location.data,
            form.twitch_handle.data
        )
        """this next bit could probably be done just in the template, now that the session object is available to jinja."""
    return flask.render_template(
        'content_gamer_profile.html', form=form, profile=profile, auth=auth, fundraisers=fundraisers)
