import flask
import flask_admin
from flask_admin.contrib.sqla import ModelView

from pyg.web import db, models


class SessionProxy(object):

    def __getattr__(self, key, *args, **kwargs):
        return getattr(db.web.session, key, *args, **kwargs)


def init(app):
    app.config['FLASK_ADMIN_SWATCH'] = 'simplex'
    admin = flask_admin.Admin(
        app,
        name='PawsYourGame',
        template_mode='bootstrap3')
    session = SessionProxy()

    class TextAdmin(ModelView):
        can_create = False
        can_delete = False
        can_edit = True
        list_columns = ['route_id', 'slug', 'text']
        form_columns = ['route_id', 'slug', 'text']
        column_filters = ['route_id']
        column_searchable_list = ['route_id']
        column_editable_list = ['text']
        form_args = dict(
            route_id=dict(render_kw={'readonly': 'readonly'}),
            slug=dict(render_kw={'readonly': 'readonly'}),)

    class RouteAdmin(ModelView):
        can_create = False
        can_delete = False
        can_edit = True
        list_columns = ['id', 'texts']
        form_columns = ['texts']
        inline_models = (TextAdmin(models.Text, session),)

    admin.add_view(ModelView(models.Member, session))
    admin.add_view(ModelView(models.Auth, session))
    admin.add_view(ModelView(models.Team, session))
    admin.add_view(ModelView(models.Donation, session))
    admin.add_view(ModelView(models.NewsArticle, session))
    admin.add_view(RouteAdmin(models.Route, session))
    admin.add_view(TextAdmin(models.Text, session))
