import flask
import sys

from sqlalchemy import func, desc

from pyg.web import db, models

bp = flask.Blueprint('search', __name__)



@bp.route('/search', methods=['GET', 'POST'])
def search():
    if flask.request.method == 'POST':
        donations = db.web.session.query(
            models.Profile.handle,
            func.sum(models.Donation.amount).label('total')
        ).join(models.Member.profile
               ).join(models.Donation
                      ).group_by(
            models.Profile.handle).order_by(desc('total')).all()
        ranked = enumerate(donations, start=1)
        searchname = flask.request.form['name']
        return flask.render_template(
            'content_search.html', donations=ranked)
    else:

        return flask.render_template('content_search.html')
