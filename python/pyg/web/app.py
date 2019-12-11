import sys
import os
import mimetypes
import pkg_resources

import flask
from oscar import flag
from twisted.python import log
from jinja2 import PackageLoader
from werkzeug import exceptions
from flask_login import LoginManager

import pyg.web
from pyg.web.views import login, home, signup, news, search, about, teamprofile, userprofile
from pyg.web import container
from pyg.web import db, testing_data


FLAGS = flag.namespace(__name__)
FLAGS.endpoint = flag.String("server endpoint", default="tcp:8080")
FLAGS.debug = flag.Bool("enable debug", default=False)


"""this class and the following two functions enable loading static assets from the .pex"""


class PexFlask(flask.Flask):

    def send_static_file(self, filename):
        if not self.has_static_folder:
            raise RuntimeError('No static folder for this object')
        # Ensure get_send_file_max_age is called in all cases.
        # Here, we ensure get_send_file_max_age is called for Blueprints.
        cache_timeout = self.get_send_file_max_age(filename)
        # Get the relative static directory
        directory = os.path.relpath(self.static_folder, self.root_path)

        return send_from_package("pyg.web", directory,
                                 filename, cache_timeout=cache_timeout)


def send_from_package(package, directory, filename, **options):
    fp = read_from_package(package, directory, filename)
    options.setdefault('conditional', True)

    mimetype = mimetypes.MimeTypes().guess_type(filename, strict=False)[0]

    try:
        return flask.send_file(fp, mimetype=mimetype, **options)
    except ValueError:
        print("still having mimetype problems. See app.py")
        mimetype = "application/octet stream"
        return flask.send_file(fp, mimetype=mimetype, **options)


def read_from_package(package, directory, filename):
    resource_location = "/".join((directory, filename,))
    if not pkg_resources.resource_exists(package, resource_location):
        print("could not find package {}".format(package))
        raise exceptions.NotFound()

    return pkg_resources.resource_stream(package, resource_location)


"""create the app and configure it."""
app = PexFlask(__name__, static_folder='static')
app.jinja_loader = PackageLoader('pyg.web', 'templates')
# Necessary to set cookies.  Move to config later.
app.secret_key = "2380b817f0f6dc67cebcc4068fc6b437"
login_manager = LoginManager()  # part of flask-login.  Not yet implemented.


@login_manager.user_loader
def load_user(userid):
    return LoginUser(userid)


def init():
    app.register_blueprint(login.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(signup.bp)
    app.register_blueprint(news.bp, url_prefix='/news')
    app.register_blueprint(about.bp)
    app.register_blueprint(teamprofile.bp)
    app.register_blueprint(search.bp)
    app.register_blueprint(userprofile.bp)
    db.init(app)
    login_manager.init_app(app)
    testing_data.makesomeboyees
    return app


def main():
    init()
    container.run(app, FLAGS.endpoint, FLAGS.debug)


if __name__ == "__main__":
    observer = log.PythonLoggingObserver(loggerName='logname')
    observer.start()
    flag.parse_commandline(sys.argv[1:])
    flag.die_on_missing_required()
    main()
