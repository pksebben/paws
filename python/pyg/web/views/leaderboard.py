import flask
import sys

from sqlalchemy import func, desc

from pyg.web import models, db

bp =flask.Blueprint('leaderboard', __name__)

"""TODO: This next module is not finished.  Finish him!"""
# def pull_leaders(listsize = None, center = None):
#     donations = db.web.session.query(
#         models.Member.handle,
#         func.sum(models.Donation.amount).label('total')
#     ).join(models.Donation
#     ).group_by(
#         models.Profile.handle).order_by(desc('total'))
#     if listsize:
#         donations = donations.limit(listsize)
#     if center:
#         donations = donations.offset()
#     leaderlist = enumerate(donations, start=1)
#     return leaderlist

@bp.route('/leaderboard')
def leaderboard():
    donations = db.web.session.query(
        models.Member.handle,
        func.sum(models.Donation.amount).label('total')
    ).join(models.Donation
    ).group_by(
        models.Profile.handle).order_by(desc('total')).all()
    ranked = enumerate(donations, start=1)
    return flask.render_template('content_leaderboard.html', players = ranked)
