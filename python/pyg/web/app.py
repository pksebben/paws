import os
import mimetypes
import pkg_resources
import locale

import flask
# TODO (ben) : is environment used in this context?
from jinja2 import PackageLoader, environment
from werkzeug import exceptions
# TODO (ben) : is secure_filename used?
from werkzeug.utils import secure_filename
from flask_humanize import Humanize

import pyg.web
from pyg.web.views import login, home, signup, news, search, about, teamprofile, memberprofile, leaderboard, logout, fundraiser, create_fundraiser, account_management, partnering, account_deleted, shelterprofile, avatar_upload, donate


"""
App.py

a note for those familiar with flask:
Many of the functions that a traditional app.py handle in a flask app have been moved to run.py (such as the actual running of the app).  This was done to avoid a circular import problem relating to (I can't quite remember if it was the CMS or test suite or both.)

Things this app.py still does:
-provides an interface for the app and it's static assets in the PexFlask class that solves an earlier issue with running the app as a .pex executable (see Pantsbuild docs for more on that)
-registers all views
-configures methods and data available to templates
-performs some basic app configurations

TODO (ben) : Implement some form of UAC that uses auth tokens instead of checking userids against the session.  For more information look at The webapp hackers handbook in ch 8

TODO (ben) : When the session is passed to the template, does that expose it in an unsecure fashion? Investigate.
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
# TODO (ben) : RTFM on flask secret keys for best practices on where to
# put this.
app.secret_key = "2380b817f0f6dc67cebcc4068fc6b437"

"""
A couple of notes on the init()----

Blueprint registration:
To make a view:
1. Create the (viewname).py in /views/, with all local methods
2. Each view gets a template in /templates/, rendered in the (viewname).py
3. Call app.register_blueprint((viewname).bp) in init() below

Template Filters and Context Processors:
These are global to the app and made available to all views and templates.

"""


def init():
    # TODO (ben) : Make sure all these views are still used and prune if not
    app.register_blueprint(login.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(signup.bp)
    app.register_blueprint(news.bp, url_prefix='/news')
    app.register_blueprint(search.bp)
    app.register_blueprint(about.bp)
    app.register_blueprint(teamprofile.bp)
    app.register_blueprint(memberprofile.bp)
    app.register_blueprint(leaderboard.bp)
    app.register_blueprint(logout.bp)
    app.register_blueprint(fundraiser.bp)
    app.register_blueprint(create_fundraiser.bp)
    app.register_blueprint(account_management.bp)
    app.register_blueprint(partnering.bp)
    app.register_blueprint(account_deleted.bp)
    app.register_blueprint(shelterprofile.bp)
    app.register_blueprint(avatar_upload.bp)
    app.register_blueprint(donate.bp)
    
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    humanize = Humanize(app)
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    # TODO (ben) : do we use all of these?  Are we still providing the session
    # as a global context proc?
    @app.template_filter()
    def format_currency(value):
        return locale.currency(value, symbol=True, grouping=True)

    @humanize.localeselector
    def get_locale():
        return 'en_US'

    @app.context_processor
    def provideloginform():
        loginform = login.LoginForm(flask.request.form)
        return {'loginform': loginform}

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
