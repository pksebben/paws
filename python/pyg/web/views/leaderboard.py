import flask
import sys

from sqlalchemy import func, desc

from pyg.web import models, db

bp = flask.Blueprint('leaderboard', __name__)

"""
Leaderboard view
This module is under a bit of limbo at the moment.  The leaderboard itself was factored out so the view it references no longer exists.  We may or may not want to do something about this, dependant on whether we find it useful to have a dedicated leaderboard page.

IMPORTANT QUESTION:
What purpose would a dedicated leaderboard serve that is not served by having leaderboards in the home page / fundraiser pages / team pages?

TODO:
- Create a leaderboard page that uses the leaderboard macro in 'leaderboard.html'
- This next module is not finished.  Finish him!

CURRENTLY:
We want to make it such that the leaderboard function serves up a 'windowed' version of the data.
"""


"""
This query defines a 'window' of players to look at that are X ahead of the chosen member and X behind (vis a vis Starcrack).

It is required anywhere you want to serve up such an asset.
"""
def rankedlist(member, windowsize=3):
    donations = db.web.session.query(
        models.Member.handle,
        models.Member.rank,
        func.sum(models.Donation.amount).label('total')
    ).join(models.Donation
           ).group_by(
        models.Member.handle).order_by(desc(models.Member.rank)).filter(models.Member.rank + windowsize >= member.rank, models.Member.rank - windowsize <= member.rank)
    return donations


@bp.route('/leaderboard')
def leaderboard():
    donations = db.web.session.query(
        models.Member.handle,
        func.sum(models.Donation.amount).label('total')
    ).join(models.Donation
           ).group_by(
        models.Member.handle).order_by(desc('total')).all()
    # ranked = enumerate(donations, start=1)
    ranked = rankedlist(db.web.session.query(models.Member).get(15))
    return flask.render_template(
        'content_leaderboard.html', leaderboard_players=ranked)
