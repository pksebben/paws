import logging
import sys

import structlog
from structlog import twisted
from structlog.twisted import LoggerFactory
from oscar import flag
from twisted.python import log
from twisted.internet import task, reactor
from sqlalchemy import func, desc
from twisted.internet import task
from twisted.internet import reactor

from pyg.web import admin, app, container, db, models

"""Ranking func
Uses the twisted LoopingCall to schedule a repeating function that queries the db , organizing by sum(donations) 
"""
def set_ranks():
    if db.web is not None:
        members = db.web.session.query(
            models.Member,
            func.sum(
                models.Donation.amount).label('total')).join(
                    models.Donation).group_by(
                        models.Member).order_by(
                            desc('total')).all()
        for i in range(len(members)):
            members[i][0].rank = i
            
        db.web.session.commit()

l = task.LoopingCall(set_ranks)
l.start(60.0) # call every second

# l.stop() will stop the looping calls

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
    app.app.jinja_env.auto_reload = True
    # reactor.run()
    set_ranks()
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
