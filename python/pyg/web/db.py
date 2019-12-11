from oscar import flag

from pyg.web import plugin
from pyg.web import models


FLAGS = flag.namespace(__name__)
FLAGS.web = flag.String("web db connection string", default="sqlite:///foo.db")


web = None


def init(app):
    global web
    web = plugin.SQLAlchemy(app, FLAGS.web)
    models.Base.metadata.create_all(web.engine)
