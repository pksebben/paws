import sys

import flask
from oscar import flag
from .sqlwizardry import SQLAlchemy
from sqlalchemy import create_engine

import pyg.web
from pyg.web import api
from pyg.web import container
from pyg.web import models


FLAGS = flag.namespace(__name__)
FLAGS.endpoint = flag.String("server endpoint", default=flag.REQUIRED)
FLAGS.debug = flag.Bool("enable debug", default=False)

app = flask.Flask(__name__)

# Do we want to put the database URI in a config file?
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://coffee:wildseven@localhost:5432/coffee"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#TODO: factor out database population and database configs
engine = create_engine("postgresql://coffee:wildseven@localhost:5432/coffee")

models.Base.metadata.create_all(engine)


def create_app():
    # TODO: everything
    app.register_blueprint(api.bp)
    return app


def main():
    container.run(create_app(), FLAGS.endpoint, FLAGS.debug)

    
if __name__ == "__main__":
    flag.parse_commandline(sys.argv[1:])
    flag.die_on_missing_required()
    main()
