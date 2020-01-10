import flask
import sys

from sqlalchemy import func, desc

from pyg.web import db, models


"""
Search page
This is a combination search and sort view that is the single source of direct access to all team, fundraiser, member profiles.

This page, once complete, should have the following functions:
Search for or Browse
-Members
--who are streamers
--who are just members
--who own team pages
--who own shelters
-Shelters
-Teams
-Fundraisers
Order results by
-cash raised (members fundraisers teams)
-start/end dates (in the case of fundraisers)
-profile age (teams and shelters)
-members (fundraisers and teams)
-location (shelters)
-probably more, but it's late today and my brain is fried.


TODO:
- Basically everything.  There's a ton of awkward SQL necessary to perform the correct sorting on all of these so I haven't gotten terribly far yet.
"""

bp = flask.Blueprint('search', __name__)


@bp.route('/search', methods=['GET', 'POST'])
def search():
    if flask.request.method == 'POST':
        donations = db.web.session.query(
            models.Member.handle,
            func.sum(models.Donation.amount).label('total')
        ).join(models.Donation
               ).group_by(
            models.Member.handle).order_by(desc('total')).all()
        ranked = enumerate(donations, start=1)
        searchname = flask.request.form['name']
        return flask.render_template(
            'content_search.html', donations=ranked)
    else:

        return flask.render_template('content_search.html')
