from oscar import flag
from sqlalchemy.orm import scoped_session, sessionmaker

from pyg.web import plugin
from pyg.web import models


FLAGS = flag.namespace(__name__)
FLAGS.web = flag.String("web db connection string", default="sqlite:///foo.db")


web = None
# db_session = None

def init(app):
    global web
    # global db_session
    web = plugin.SQLAlchemy(app, FLAGS.web)
    # db_session = scoped_session(sessionmaker(autocommit=False,
    #                                          autoflush=False,
    #                                          bind=web.engine))
    models.Base.metadata.create_all(web.engine)
