from __future__ import absolute_import

import threading

import sqlalchemy
from sqlalchemy import orm



"""
plugin.py
This mysteriously-named little gem provides an interface between flask and SQLAlchemy, functionally parallel to flask-sqlalchemy but without all the spooky action-at-a-distance and weird side effects.  Ian wrote it, so if it's fucked up go talk to him first.

WARNING: At least on three seperate occassions (that I can think of right now) other third-party flask modules have expected use of flask-sqlalchemy and in only one of them was this not a breaking interaction.  The design decision to use this relates to keeping the important code present and readable and NOT buried under a mountain of 'assumptions-some-other-douchebag-made'.  Be careful when implementing third-party flask plugins to make sure that they don't mention assumptions re: flask-sqlalchemy.  IF YOU DO RUN INTO A BUG YOU THINK IS RELATED: ask yourself if the extension is really doing something we cannot do ourselves.  If you absolutely cannot live without the new shiny thing, you're gonna have to ask Ian to 'fix his code' to work with yours.  Good luck.

"""

class SQLAlchemy(object):

    DEFAULT_ENGINE_CONF = {
        'pool_recycle': 1200,
    }

    DEFAULT_SESSION_CONF = {
        'autoflush': True,
        'expire_on_commit': True,
        '_enable_transaction_accounting': True,
    }

    DEFAULT_SCOPE_IDENT = threading.get_ident

    def __init__(self, app, connection_string=None,
                 engine_conf=None, session_conf=None):
        '''Create a SQLAlchemy db/session manager.

       :type app: auster.Service
       :type connection_string: str or None
       :type engine_conf: dict or None
       :type session_conf: dict or None
       '''
        self.app = app
        self.engine_conf = engine_conf or dict()
        self.session_conf = session_conf or dict()
        self.sessionmaker = None

        if connection_string is not None:
            self.init(connection_string, engine_conf, session_conf)

    def init(self, connection_string, engine_conf=None, session_conf=None):
        '''Initialize the SQLAlchemy session manager.

       :param str connection_string: database URI (e.g. sqlite:///foo.db)
       :type engine_conf: dict or None
       :type session_conf: dict or None
       '''
        self.engine_conf.update(self.DEFAULT_ENGINE_CONF)
        if engine_conf:
            self.engine_conf.update(engine_conf)
        self.session_conf.update(self.DEFAULT_SESSION_CONF)
        if session_conf:
            self.session_conf.update(session_conf)
        self.engine = sqlalchemy.create_engine(
            connection_string, **self.engine_conf)
        self.sessionmaker = orm.scoped_session(
            orm.sessionmaker(bind=self.engine, **self.session_conf),
            scopefunc = self.DEFAULT_SCOPE_IDENT)

        @self.app.teardown_request
        def _close(unused_exc, unused_func=None, unused_method=None):
            self.sessionmaker.remove()

    @property
    def session(self):
        '''The session object for this scope.'''
        return self.get_session()

    def get_session(self, session_conf=None):
        '''Create a session for this scope.

       :type session_conf: dict or None
       '''
        assert self.sessionmaker is not None, 'sqlalchemy connection not initialized'
        orm.configure_mappers()
        local_conf = session_conf or dict()
        return self.sessionmaker(**local_conf)
