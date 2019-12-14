import os
import mimetypes
import pkg_resources
import locale

import flask
from jinja2 import PackageLoader, environment
from werkzeug import exceptions
from flask_login import LoginManager
from flask_humanize import Humanize

import pyg.web
from pyg.web.views import login, home, signup, news, search, about, teamprofile, userprofile, leaderboard, logout, fundraiser, create_fundraiser


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
    app.register_blueprint(leaderboard.bp)
    app.register_blueprint(logout.bp)
    app.register_blueprint(fundraiser.bp)
    app.register_blueprint(create_fundraiser.bp)
    login_manager.init_app(app)

    humanize = Humanize(app)
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    @app.template_filter()
    def format_currency(value):
        return locale.currency(value, symbol=True, grouping=True)

    @humanize.localeselector
    def get_locale():
        return 'en_US'

    @app.context_processor
    def dynamic_data():
        texts = pyg.web.db.web.session.query(
            pyg.web.models.Text).filter_by(
                route_id=str(flask.request.url_rule))
        text_dict = {x.slug: x.text for x in texts}
        return {'text': text_dict}

    @app.context_processor
    def user_session():
        usersession = flask.session
        return usersession

    return app
