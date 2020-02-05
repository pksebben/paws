import sched
import time

from pyg.web import db, models
from sqlalchemy import func, desc


"""
this is meant to periodically crawl the database and update rankings, so they don't have to be calculated for every query

TODO: Fix up this function such that it no longer throws errors, derp.
"""

def set_ranks():
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
        
s = sched.scheduler(time.time, time.sleep)
        
def schedule_rankings():
    print("ranking...")
    set_ranks()
    s.enter(10, 1,schedule_rankings)
            
def init_ranking():
    schedule_rankings()
    s.run()
