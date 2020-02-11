import os
import datetime

import flask
from werkzeug.utils import secure_filename

from pyg.web import db, models

bp = flask.Blueprint("avatar_upload", __name__)

"""
File upload mechanism.  Under construction.
CONSTRUCTION NOTES:
- This mechanism should be factored such that it is useful on pages like member profile.
- There may be issues with the static file folder and the methods we use to serve it up here.  Look into that if you get error messages with FnF or NoneType 


"""

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/avatar_upload', methods=['POST','GET'])
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
            member = db.web.session.query(models.Member).get(flask.session['userid'])           
            filename = "av" + "_" + str(datetime.datetime.now()) + '_' + str(member.id)
            print(flask.current_app.static_folder)
            savepath = str(flask.current_app.static_folder) + '/userinfo/avatars/'
            file.save(os.path.join(savepath, filename))
            flask.flash('saved!!')

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''







