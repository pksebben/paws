from __future__ import absolute_import
 
import threading
 
import sqlalchemy
from sqlalchemy import orm
 
 
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


    """
app is the instance of a flaskapp ###############ASK IAN IF THIS IS TRUE###############
%%%%%%%%%%%%%%%IT IS!%%%%%%%%%%%%%%%

connection_string is the string the sqlalchemy engine uses to connect to the db.

engine_conf is the engine configuration, and can have the following parameters:
    bind – a Engine or other Connectable with which newly created Session objects will be associated.
    class_ – class to use in order to create new Session objects. Defaults to Session.
    autoflush – The autoflush setting to use with newly created Session objects.
    autocommit – The autocommit setting to use with newly created Session objects.
    expire_on_commit=True – the expire_on_commit setting to use with newly created Session objects.
    info – optional dictionary of information that will be available via Session.info. Note this dictionary is updated, not replaced, when the info parameter is specified to the specific Session construction operation.
    New in version 0.9.0.
    **kw – all other keyword arguments are passed to the constructor of newly created Session objects.

session_conf is, predictably, the session configuration, and can have the following:
    autocommit - don't use this.
    autoflush – When True, all query operations will issue a flush() call to this Session before proceeding. This is a convenience feature so that flush() need not be called repeatedly in order for database queries to retrieve results. It’s typical that autoflush is used in conjunction with autocommit=False. In this scenario, explicit calls to flush() are rarely needed; you usually only need to call commit() (which flushes) to finalize changes.
    bind – An optional Engine or Connection to which this Session should be bound. When specified, all SQL operations performed by this session will execute via this connectable.
    binds – A dictionary which may specify any number of Engine or Connection objects as the source of connectivity for SQL operations on a per-entity basis. The keys of the dictionary consist of any series of mapped classes, arbitrary Python classes that are bases for mapped classes, Table objects and Mapper objects. The values of the dictionary are then instances of Engine or less commonly Connection objects. Operations which proceed relative to a particular mapped class will consult this dictionary for the closest matching entity in order to determine which Engine should be used for a particular SQL operation. The complete heuristics for resolution are described at Session.get_bind(). Usage looks like:
    Session = sessionmaker(binds={
    SomeMappedClass: create_engine('postgresql://engine1'),
    SomeDeclarativeBase: create_engine('postgresql://engine2'),
    some_mapper: create_engine('postgresql://engine3'),
    some_table: create_engine('postgresql://engine4'),
    })
    SEE ALSO
    Session.bind_mapper()
    Session.bind_table()
    Session.get_bind()
    class_ – Specify an alternate class other than sqlalchemy.orm.session.Session which should be used by the returned class. This is the only argument that is local to the sessionmaker function, and is not sent directly to the constructor for Session.
    enable_baked_queries – defaults to True. A flag consumed by the sqlalchemy.ext.baked extension to determine if “baked queries” should be cached, as is the normal operation of this extension. When set to False, all caching is disabled, including baked queries defined by the calling application as well as those used internally. Setting this flag to False can significantly reduce memory use, however will also degrade performance for those areas that make use of baked queries (such as relationship loaders). Additionally, baked query logic in the calling application or potentially within the ORM that may be malfunctioning due to cache key collisions or similar can be flagged by observing if this flag resolves the issue.
    New in version 1.2.
    _enable_transaction_accounting – A legacy-only flag which when False disables all 0.5-style object accounting on transaction boundaries.
    expire_on_commit – Defaults to True. When True, all instances will be fully expired after each commit(), so that all attribute/object access subsequent to a completed transaction will load from the most recent database state.
    extension – use sessionEvents instead
    info – optional dictionary of arbitrary data to be associated with this Session. Is available via the Session.info attribute. Note the dictionary is copied at construction time so that modifications to the per- Session dictionary will be local to that Session.
    New in version 0.9.0.
    query_cls – Class which should be used to create new Query objects, as returned by the query() method. Defaults to Query.
    twophase – When True, all transactions will be started as a “two phase” transaction, i.e. using the “two phase” semantics of the database in use along with an XID. During a commit(), after flush() has been issued for all attached databases, the prepare() method on each database’s TwoPhaseTransaction will be called. This allows each database to roll back the entire transaction, before each transaction is committed.
    weak_identity_map – don't use it.

    """
    def __init__(self, app, connection_string=None, engine_conf=None, session_conf=None):
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
        """
        sqlalchemy.create_engine(connectionstring, [configuration])
        creates an instance of Engine which essentially preconfigures a set of parameters to create connections to the database.
        Enigine.connectionstring is all the stuff you need to connect to the engine.  Starting with the dialect for the type of database (e.g. mySQL, PostGres), followed by ://[username]:[password], ending with @[URL]/[nameofdatabase]
        
        """
        self.engine = sqlalchemy.create_engine(connection_string, **self.engine_conf)
        """
        Sessionmaker (sqlalchemy.orm.session.sessionmaker)
        sessionmaker is a factory for Session objects.  It takes a connection object from an engine (created in this case with create_engine()), and stores details to be committed on session.commit.
        1.BINDING A SESSION TO AN ENGINE
        Session = sessionmaker(bind=[some_engine])  //this creates a bound Session class, but no instances, yet.
        2.CREATING AN ACTUAL, REAL SESSION
        session = Session()  // this creates the session instance.
        3.ADD SHIT TO A SESSION
        someobject = SomeObject('foo','bar')
        session.add(someobject)
        4.COMMIT THE SESSION
        session.commit()

        
        the sqlalchemy docs talk about scoped_session(), which is a layer between the session factory (1) and session instances (2).  It represents a registry of session objects, and allows different modules to reliably utilise the same session object by proxying sessions that are committed to it.  Essentially, this prevents creating more than one session at a time of the same session factory pattern, and allows access to that session object agnostic of origin so long as the calling function is in the scope of the class that called scoped_session.  THIS MEANS that you don't need to worry about session scope in other modules so long as you call them from within this class.

        What's happening here:
    self.sessionmaker = orm.scoped_session(
        self.sessionmaker is simply an object tied to this SQLAlchemy class.  It's being set to a scoped_session (that is, registered as the current session in this scope) by orm.scoped_session
    orm.sessionmaker(bind=self.engine, **self.session_conf),
        this is the session_factory kwarg required by orm.scoped_session().  Here we use sessionmaker to create a session object bound to whatever engine is defined in self.engine with configuration = self.session_conf
    scopefunc = self.DEFAULT_SCOPE_IDENT
        DEFAULT_SCOPE_IDENT is, at the moment of this writing, set to threading.get_ident(), which returns a 'magic cookie' pointing to thread-specific data.  This line defines the scope of the scoped_session as the current thread.
###############ASK IAN ABOUT THIS###############
        I don't know much about threads, so what does this scoping mean, exactly?  That we have to call all functions for this scoped session in sequence? in the same module? does it mean that we simply shouldn't do async shit in between session calls?
        """
        self.sessionmaker = orm.scoped_session(
            orm.sessionmaker(bind=self.engine, **self.session_conf),
            scopefunc=self.DEFAULT_SCOPE_IDENT)
 
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
        """
        orm.configure_mappers() doesn't seem to add any mappers by itself, but instead kinda smooshes em all together in an attempt to relate the mappers to each other?  (the docs talk about inter-mapper relationships, which I can't imagine to mean anything else).
###############ASK AN IAN!###############
where the fuchk do we add the actual mappings to the section?  SESSION_CONF.binds?
%%%%%%%%%%%%%%%answered%%%%%%%%%%%%%%%
if the object is defined as db = ThisClass(**kwargs), then...
db.session.add(all the shit)
        """
        orm.configure_mappers()
        local_conf = session_conf or dict()
        return self.sessionmaker(**local_conf)


"""
GIST
this module creates sessions to connect the flask app to the database, configuring and handling those sessions while scoping them to a common thread.

to make use of a session, use session.add() on an appropriate deserialized object (like from marshmallow).

FOR EASY PEASY CONCEPTS OF USE
refer to sqlalchemy's Session tutorial, look at the top, and change any session. to db.session.
"""
