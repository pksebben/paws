from oscar import flag
from sqlalchemy.orm import scoped_session, sessionmaker

from pyg.web import plugin
from pyg.web import models


"""
db.py
Prepares the database and serves as an interface to that db.
This is the module you need to use to get the sqlalchemy session, done like so:
db.web.session.query(models.Foo)
For more information, see the terribly convoluted SQLAlchemy docs.  Start with the tutorial sections if you're unsure of where to start, as that's pretty much the only semi-intuitive part of their docs.

"""

FLAGS = flag.namespace(__name__)
FLAGS.web = flag.String("web db connection string", default="sqlite:///foo.db")


web = None

def init(app):
    global web
    web = plugin.SQLAlchemy(app, FLAGS.web)
    models.Base.metadata.create_all(web.engine)
