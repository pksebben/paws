import sys
import os
import io
import mimetypes
import pkg_resources

import flask
from oscar import flag
from sqlalchemy import create_engine
from twisted.python import log
from jinja2 import PackageLoader
from werkzeug import exceptions

import pyg.web
from pyg.web import api
from pyg.web import container
from pyg.web import models
from pyg.web import db
from pyg.web import plugin



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
        print("mimetype guessing failed. setting mime to octet")
        mimetype = "application/octet stream"
        return flask.send_file(fp, mimetype=mimetype, **options)


def read_from_package(package, directory, filename):
    resource_location = "/".join((directory, filename,))
    if not pkg_resources.resource_exists(package, resource_location):
        print("resource does not exist")
        print("resource location is")
        print(resource_location)
        print("package is")
        print(package)
        print("directory is ")
        print(directory)
        print("filename is")
        print(filename)
        raise exceptions.NotFound()

    return pkg_resources.resource_stream(package, resource_location)


app = PexFlask(__name__ ,static_folder='static')

app.jinja_loader = PackageLoader('pyg.web','templates')

print("stderr is working", file=sys.stderr)

def create_app():
    app.register_blueprint(api.bp)
    db.init(app)
    return app


def main():
    container.run(create_app(), FLAGS.endpoint, FLAGS.debug)


if __name__ == "__main__":
    observer = log.PythonLoggingObserver(loggerName='logname')
    observer.start()
    flag.parse_commandline(sys.argv[1:])
    flag.die_on_missing_required()
    main()
