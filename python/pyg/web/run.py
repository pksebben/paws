import sys
import pdb

import structlog
from structlog import twisted
from oscar import flag
from twisted.python import log
from twisted.internet import task
from sqlalchemy import func, desc

from pyg.web import admin, app, container, db, models


"""
run.py
This was factored out of app.py because of some circular import problem
relating to the test suite or admin panel or some such.

See app.py for a more detailed explanation of what got moved and what didn't.

Things that happen here:
-logging config
-app and db init()

"""


# TODO: Refactor to somewhere it makes sense.
def set_ranks():
    """calculate ranks for member table """
    if db.web is not None:
        members = db.web.session.query(
            models.Member,
            func.sum(
                models.Donation.amount).label('total')).join(
                    models.Donation).group_by(
                        models.Member).order_by(
                            desc('total')).all()
        for i in enumerate(members):
            i[1][0].rank = i[0]

        db.web.session.commit()
    else:
        raise Exception("no database found")


# TODO: (*1) Refactor into server calls.  See below.
# There are likely a number of "looping call" functions we are going to need.
def init_ranks():
    """run set_ranks every minute"""
    rankloop = task.LoopingCall(set_ranks)
    rankloop.start(60.0)  # call every second


FLAGS = flag.namespace(__name__)
FLAGS.endpoint = flag.String("server endpoint", default="tcp:8080") #TODO: default is non-functional ATM.  Troubleshoot. 
FLAGS.debug = flag.Bool("enable debug", default=False)
logger = structlog.get_logger() #TODO: This belongs in an init() 


def main():
    """Initialize app, db, admin panel, and run the container"""
    app.init()
    db.init(app.app)
    init_ranks()                #TODO: Refactor.  See *1 
    admin.init(app.app)
    app.app.jinja_env.auto_reload = True
    set_ranks()                 # TODO: this should live in app.init()
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
