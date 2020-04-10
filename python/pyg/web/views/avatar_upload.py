import os
import datetime

import flask
from werkzeug.utils import secure_filename

from pyg.web import db, models

bp = flask.Blueprint("avatar_upload", __name__)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


"""
Avatar Upload
Members may upload avatars in {what formats?}.  The file will live in /static/avatars/ 

Avatar image names are automatically applied as the image uploads (In order to circumvent directory traversal attacks), and take the format { 'av_' + timestamp + '_' + member id }.  This name is saved in the 'avatar url' field in their profile table. 

This route will eventually become an api call and reroute to the member profile page.
TODO(ben): Validation errors ("wrong filetype, meathead etc.")
TODO(ben): Turn this into an API call / implement in member profile

"""
@bp.route('/avatar_upload', methods=['POST', 'GET'])
def upload_file():
    if flask.request.method == 'POST':
        if 'file' not in flask.request.files:
            flask.flash('no file part')
            return flask.redirect(flask.request.url)
        file = flask.request.files['file']
        if file.filename == '':
            flask.flash('no selected file')
            return flask.redirect(flask.request.url)
        if file and allowed_file(file.filename):
            # place a pointer in the db and make it the filename
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
            flask.flash('saved!!')

    return flask.render_template("upload_avatar.html")
