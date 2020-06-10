import os
import datetime
import imghdr

import flask
from wtforms import Form, FileField, validators, ValidationError

from pyg.web import db, models

bp = flask.Blueprint("avatar_upload", __name__)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def invalid_filetype(form, field):
    """if this ends up working, leave the rest of this docstring
this validator always fails.  It is meant to be called IOT cause wtforms to properly display a validation message.
It is a (terribly hacky) workaround for the fact that wtforms does not actually wrap the fileupload field around the file data to be uploaded.  Why they would even bother having such a field, IDK.  maybe it works in places other than flask.  Shit design, IMHO.
 """
    print("filetype invalidated")
    raise ValidationError(
        "Invalid filetype.  Please upload a jpg, png, or gif.")


"""
Avatar Upload
Members may upload avatars in {what formats?}.  The file will live in /static/avatars/

Avatar image names are automatically applied as the image uploads (In order to circumvent directory traversal attacks), and take the format { 'av_' + timestamp + '_' + member id }.  This name is saved in the 'avatar url' field in their profile table.

This route will eventually become an api call and reroute to the member profile page.
TODO(ben): Turn this into an API call / implement in member profile
"""


class UploadForm(Form):
    avatar = FileField(validators=[])


@bp.route('/avatar_upload', methods=['POST', 'GET'])
def upload_file():
    avatarform = UploadForm(flask.request.form)
    if flask.request.method == 'POST' and avatarform.validate():
        if 'avatar' not in flask.request.files:
            print('no file uploaded')
            return flask.redirect(flask.request.url)
        file = flask.request.files['avatar']
        if file.filename == '':
            print('no selected file')
            return flask.redirect(flask.request.url)
        # if imghdr.what(file) in ['jpg', 'png','jpeg']:
        #     print("IMGHDR FILE TYPE CHECKING WORKS")
        #     print(imghdr.what(file))
        # else:
        #     print("IMGHDR NOT WORKING")
        #     print(imghdr.what(file))
        if file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS or imghdr.what(file) in ALLOWED_EXTENSIONS:
            # do uploady stuff
            member = db.web.session.query(
                models.Member).get(
                flask.session['userid'])
            filename = "av" + "_" + \
                str(datetime.datetime.now()) + '_' + str(member.id)
            savepath = str(flask.current_app.static_folder) + \
                '/userinfo/avatars/'
            file.save(os.path.join(savepath, filename))
            print(filename)
            member.avatar_url = str(filename)
            db.web.session.commit()
            print('saved!!')
            gotostr = "/profile/" + str(flask.session['userid'])
            return flask.redirect(gotostr)
        else:
            avatarform.avatar.validate(avatarform, extra_validators=[invalid_filetype])
            return flask.render_template("upload_avatar.html", avatarform=avatarform)
            # place a pointer in the db and make it the filename
    return flask.render_template(
        "upload_avatar.html", avatarform=avatarform)
