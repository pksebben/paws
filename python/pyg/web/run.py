import logging
import sys

import structlog
from structlog import twisted
from structlog.twisted import LoggerFactory
from oscar import flag
from twisted.python import log

from pyg.web import app, container, db

FLAGS = flag.namespace(__name__)
FLAGS.endpoint = flag.String("server endpoint", default="tcp:8080")
FLAGS.debug = flag.Bool("enable debug", default=False)
logger = structlog.get_logger()


def main():
    app.init()
    db.init(app.app)
    container.run(app.app, FLAGS.endpoint, FLAGS.debug)


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    # structlog.configure(
    #     processors=[twisted.EventAdapter()],
    #     logger_factory=twisted.LoggerFactory(),
    #     wrapper_class=twisted.BoundLogger,
    #     cache_logger_on_first_use=True
    # )
    log.startLogging(sys.stderr)
    observer = log.PythonLoggingObserver(loggerName='logname')
    observer.start()
    
    flag.parse_commandline(sys.argv[1:])
    flag.die_on_missing_required()
    main()
