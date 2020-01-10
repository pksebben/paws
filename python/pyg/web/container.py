import logging

from oscar import flag
from twisted.internet import endpoints
from twisted.internet import reactor
from twisted.python import log
from twisted.web import server
from twisted.web import wsgi



"""
container.py
I'm gonna be honest, I have *no idea* what this does.

TODO:
- essplain me what dafuq dis be, bossman.

"""

logger = logging.getLogger(__name__)

FLAGS = flag.namespace(__name__)
FLAGS.threadpool_size = flag.Int('threadpool size', 20)


def run(app, address, debug):
    """Serve wsgi `app` on Twisted server endpoint `address`.

    :param app: wsgi application
    :param str address: twisted endpoint
    :param bool debug: enable debugging and reloading
    """

    def err_shutdown(failure):
        log.err(failure)
        reactor.callWhenRunning(reactor.stop)

    def _run():
        reactor.suggestThreadPoolSize(FLAGS.threadpool_size)
        resource = wsgi.WSGIResource(reactor, reactor.getThreadPool(), app)
        site = server.Site(resource)
        endpoint = endpoints.serverFromString(reactor, address)
        endpoint.listen(site).addErrback(err_shutdown)
        reactor.run(installSignalHandlers=int(not debug))

    logger.info('event=\'starting twisted\' debug=%r address=%r',
                debug, address)

    if debug:
        import werkzeug.serving
        import werkzeug.debug
        app = werkzeug.debug.DebuggedApplication(app, evalex=True)
        werkzeug.serving.run_with_reloader(_run)
    else:
        _run()
