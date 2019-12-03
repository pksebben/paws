import sys
import os
import mimetypes
import pkg_resources

import flask
from oscar import flag
from sqlalchemy import create_engine
from twisted.python import log
from jinja2 import PackageLoader
from werkzeug import exceptions
from flask_login import LoginManager

import pyg.web
from pyg.web import views
from pyg.web import container
from pyg.web import db



FLAGS = flag.namespace(__name__)
FLAGS.endpoint = flag.String("server endpoint", default=flag.REQUIRED)
FLAGS.debug = flag.Bool("enable debug", default=False)

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


app = PexFlask(__name__ ,static_folder='static')

app.jinja_loader = PackageLoader('pyg.web','templates')

# Necessary to set cookies.  Move to config later.
app.secret_key = "2380b817f0f6dc67cebcc4068fc6b437"

login_manager = LoginManager()

# incomplete
# class LoginUser(UserMixin):

#     def __init__(self, id):
#         self.id = id
#         self.name = "user" + str(id)
#         self.password = self.name + "_secret"

@login_manager.user_loader
def load_user(userid):
    return LoginUser(userid)

def create_app():
    app.register_blueprint(views.bp)
    db.init(app)
    login_manager.init_app(app)
    return app


def main():
    container.run(create_app(), FLAGS.endpoint, FLAGS.debug)


if __name__ == "__main__":
    observer = log.PythonLoggingObserver(loggerName='logname')
    observer.start()
    flag.parse_commandline(sys.argv[1:])
    flag.die_on_missing_required()
    main()
