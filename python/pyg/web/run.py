import logging
import sys

from oscar import flag
from twisted.python import log

from pyg.web import app, container, db

FLAGS = flag.namespace(__name__)
FLAGS.endpoint = flag.String("server endpoint", default="tcp:8080")
FLAGS.debug = flag.Bool("enable debug", default=False)


def main():
    app.init()
    db.init(app.app)
    container.run(app.app, FLAGS.endpoint, FLAGS.debug)


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    observer = log.PythonLoggingObserver(loggerName='logname')
    observer.start()
    flag.parse_commandline(sys.argv[1:])
    flag.die_on_missing_required()
    main()
