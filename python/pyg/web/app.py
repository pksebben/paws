import sys

import flask
from oscar import flag

import api
import container


FLAGS = flag.namespace(__name__)
FLAGS.endpoint = flag.String('server endpoint', default=flag.REQUIRED)
FLAGS.debug = flag.Bool('enable debug', default=False)


def create_app():
    app = flask.Flask(__name__)
    # TODO: everything
    app.register_blueprint(api.bp)
    return app


def main():
    container.run(create_app(), FLAGS.endpoint, FLAGS.debug)


if __name__ == '__main__':
    flag.parse_commandline(sys.argv[1:])
    flag.die_on_missing_required()
    main()
