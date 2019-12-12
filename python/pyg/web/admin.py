import flask
import flask_admin
from flask_admin.contrib.sqla import ModelView

from pyg.web import db, models


class TextAdmin(ModelView):
    list_columns = ['route_id', 'slug', 'text']
    form_columns = ['route_id', 'slug', 'text']


class RouteAdmin(ModelView):
    list_columns = ['id']
    form_columns = ['id', 'texts']


def init(app):
    app.config['FLASK_ADMIN_SWATCH'] = 'simplex'
    admin = flask_admin.Admin(
        app,
        name='PawsYourGame',
        template_mode='bootstrap3')
    admin.add_view(ModelView(models.Member, db.web.session))
    admin.add_view(ModelView(models.Auth, db.web.session))
    admin.add_view(ModelView(models.Profile, db.web.session))
    admin.add_view(ModelView(models.Team, db.web.session))
    admin.add_view(ModelView(models.Donation, db.web.session))
    admin.add_view(ModelView(models.NewsArticle, db.web.session))
    admin.add_view(RouteAdmin(models.Route, db.web.session))
    admin.add_view(TextAdmin(models.Text, db.web.session))
