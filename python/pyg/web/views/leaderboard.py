import flask
import sys

from sqlalchemy import func, desc

from pyg.web import models, db

bp =flask.Blueprint('leaderboard', __name__)

@bp.route('/leaderboard')
def leaderboard():
    donations = db.web.session.query(
        models.Profile.handle,
        func.sum(models.Donation.amount).label('total')
    ).join(models.Member.profile
    ).join(models.Donation
    ).group_by(
        models.Profile.handle).order_by(desc('total')).all()
    ranked = enumerate(donations, start=1)
    return flask.render_template('content_leaderboard.html', players = ranked)
