import os
import mimetypes
import pkg_resources
import locale

import flask
from jinja2 import PackageLoader, environment
from werkzeug import exceptions
from werkzeug.utils import secure_filename
from flask_login import LoginManager
from flask_humanize import Humanize

import pyg.web
from pyg.web.views import login, home, signup, news, search, about, teamprofile, memberprofile, leaderboard, logout, fundraiser, create_fundraiser, account_management, partnering, account_deleted, shelterprofile, avatar_upload


"""
App.py

A note for those familiar with flask:
Many of the functions that a traditional app.py handle in a flask app have been moved to run.py (such as the actual running of the app).  This was done to avoid a circular import problem relating to (I can't quite remember if it was the CMS or test suite or both.)

Things this app.py still does:
-provides an interface for the app and it's static assets in the PexFlask class that solves an earlier issue with running the app as a .pex executable (see Pantsbuild docs for more on that)
-registers all views
-configures methods and data available to templates
-performs some basic app configurations

see below docstrings for more info


"""

# Upload Configuration
UPLOAD_FOLDER = '/static/uploads'


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


# TODO: Is this deprecated?
@login_manager.user_loader
def load_user(userid):
    return LoginUser(userid)


"""
A couple of notes on the init()----

Blueprint registration:
The pattern we are using requires a few things to be in place for each blueprint:
1. There must be a view for the blueprint in /views/, which should contain all the methods pertinent to that view and register a blueprint as bp.  Any of the existing views can be referred to re: the specifics of this pattern
2. The view in question should reference a template (in the case that it presents any client-facing interface) in /templates/
3. The view should be imported in this module and registered according to the pattern visible below.

Template Filters and Context Processors:
All template filters and context processors (methods for mutating data within templates or providing data to templates, respectively) are registered here.  See below the @app.foo decorators.

"""


def init():
    app.register_blueprint(shelterprofile.bp)
    app.register_blueprint(account_management.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(signup.bp)
    app.register_blueprint(news.bp, url_prefix='/news')
    app.register_blueprint(about.bp)
    app.register_blueprint(teamprofile.bp)
    app.register_blueprint(search.bp)
    app.register_blueprint(memberprofile.bp)
    app.register_blueprint(leaderboard.bp)
    app.register_blueprint(logout.bp)
    app.register_blueprint(fundraiser.bp)
    app.register_blueprint(create_fundraiser.bp)
    app.register_blueprint(partnering.bp)
    app.register_blueprint(account_deleted.bp)
    app.register_blueprint(avatar_upload.bp)
    login_manager.init_app(app)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
