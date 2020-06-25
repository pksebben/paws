import flask
import sys

from sqlalchemy import func, asc

from pyg.web import models, db

bp = flask.Blueprint('leaderboard', __name__)

"""
Leaderboard view
Test view for the leaderboard module and leaderboard population functions

This query defines a 'window' of players to look at that are X ahead of the chosen member and X behind (vis a vis Starcrack).

It is required anywhere you want to serve up such an asset.
"""


def rankedlist(member, windowsize=2):
    donations = db.web.session.query(
        models.Member.id,
        models.Member.handle,
        models.Member.rank,
        models.Member.avatar_url,
        func.sum(models.Donation.amount).label('total')
    ).join(models.Donation
           ).group_by(
        models.Member.handle).order_by(asc(models.Member.rank)).filter((models.Member.rank + windowsize) >= member.rank, (models.Member.rank - windowsize) <= member.rank)
    return donations


@bp.route('/leaderboard')
def leaderboard():
    ranked = rankedlist(db.web.session.query(models.Member).get(15))
    return flask.render_template(
        'content_leaderboard.html', leaderboard_players=ranked)
