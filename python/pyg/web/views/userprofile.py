import flask

from pyg.web import db, models

bp = flask.Blueprint("userprofile", __name__)


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
    try:
        user = db.web.session.query(models.Member).get(userid)
        auth = user.auth
        profile = user
        fundraisers = user.fundraisers
    except AttributeError as err:
        # how are we going to handle bad values for userid?
        # we want to avoid rendering the page, for sure.
        # we want something logged
        raise err
    if flask.request.method == 'POST':
        update_user_profile(
            userid,
            flask.request.form['name'],
            flask.request.form['about'],
            flask.request.form['location'],
            flask.request.form['twitch_handle']
        )
        """this next bit could probably be done just in the template, now that the session object is available to jinja."""
    if flask.session.get('userid'):
        if flask.session['userid'] == int(userid):
            # show the profile with editable fields
            return flask.render_template(
                'content_gamer_profile.html', editmode=True, profile=profile, auth=auth, fundraisers=fundraisers)
        else:
            return flask.render_template(
                "content_gamer_profile.html", editmode=False, profile=profile, auth=auth, fundraisers=fundraisers)
    else:
        # show the profile static
        return flask.render_template(
            'content_gamer_profile.html', editmode=False, profile=profile, auth=auth, fundraisers=fundraisers)
