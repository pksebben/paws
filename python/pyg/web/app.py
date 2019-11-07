import sys

import flask
from oscar import flag
from sqlalchemy import create_engine

import pyg.web
from pyg.web import api
from pyg.web import container
from pyg.web import models
from pyg.web import db
from pyg.web import plugin

from twisted.python import log


FLAGS = flag.namespace(__name__)
FLAGS.endpoint = flag.String("server endpoint", default=flag.REQUIRED)
FLAGS.debug = flag.Bool("enable debug", default=False)

app = flask.Flask(__name__)

def create_app():
    # TODO: everything
    app.register_blueprint(api.bp)
    db.init(app)
    return app


def main():
    container.run(create_app(), FLAGS.endpoint, FLAGS.debug)

    
if __name__ == "__main__":
    observer = log.PythonLoggingObserver(loggerName='logname')
    observer.start()
    flag.parse_commandline(sys.argv[1:])
    flag.die_on_missing_required()
    main()
