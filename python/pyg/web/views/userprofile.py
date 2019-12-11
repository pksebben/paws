import flask

from pyg.web import db, models

bp = flask.Blueprint("userprofile", __name__)


def update_user_profile(id, about, birthday, location, twitch_handle):
    user = db.web.session.query(models.Person).get(id)
    if not user.profile:
        user.profile = models.UserProfile(
            about=about, birthday=birthday, location=location, twitch_handle=twitch_handle)
        # change to structlog
        # print('added user profile')
    else:
        user.profile.about = about
        user.profile.birthday = birthday
        user.profile.location = location
        user.profile.twitch_handle = twitch_handle
        # change to structlog
        # print('updated user profile')
    db.web.session.commit()
    # change to structlog
    # print("user updated")


@bp.route('/profile/<userid>', methods=['GET', 'POST'])
@bp.route('/profile')
def userprofile(userid=1):
    try:
        user = db.web.session.query(models.Person).get(userid)
        auth = user.auth
        profile = user.profile
    except AttributeError as err:
        # how are we going to handle bad values for userid?
        # we want to avoid rendering the page, for sure.
        # we want something logged
        raise err
    if flask.request.method == 'POST':
        # update the user profile with form data
        update_user_profile(
            userid,
            flask.request.form['about'],
            flask.request.form['birthday'],
            flask.request.form['location'],
            flask.request.form['twitch_handle']
        )
    if flask.session.get('userid'):
        if flask.session['userid'] == userid:
            # show the profile with editable fields
            return flask.render_template(
                'content_gamer_profile.html', editmode=True, )
    else:
        # show the profile static
        return flask.render_template(
            'content_gamer_profile.html', editmode=False)