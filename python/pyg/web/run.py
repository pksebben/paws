import logging
import sys

import structlog
from structlog import twisted
from structlog.twisted import LoggerFactory
from oscar import flag
from twisted.python import log

from pyg.web import admin, app, container, db, ranking


"""
run.py
This was factored out of app.py because of some circular import problem relating to the test suite or admin panel or some such.  See app.py for a more detailed explanation of what got moved and what didn't.

Things that happen here:
-logging config
-app and db init()


TODO:
- there's still some muck in here from flask-security.  Fix it.
- logging could probably be better.
"""

FLAGS = flag.namespace(__name__)
FLAGS.endpoint = flag.String("server endpoint", default="tcp:8080")
FLAGS.debug = flag.Bool("enable debug", default=False)
logger = structlog.get_logger()


def main():
    app.init()
    db.init(app.app)
    admin.init(app.app)
    ranking.init_ranking()
    app.app.jinja_env.auto_reload = True
    container.run(app.app, FLAGS.endpoint, FLAGS.debug)


if __name__ == "__main__":
    structlog.configure(
        processors=[twisted.EventAdapter()],
        logger_factory=twisted.LoggerFactory(),
        wrapper_class=twisted.BoundLogger,
        cache_logger_on_first_use=True
    )

    log.startLogging(sys.stderr)
    
    flag.parse_commandline(sys.argv[1:])
    flag.die_on_missing_required()
    main()
