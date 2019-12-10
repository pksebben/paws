import flask
import sys
from flask import request

from pyg.web import db, models

bp = flask.Blueprint('search', __name__)

@bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        searchname = request.form['name']
        print("testing", file=sys.stderr)
        print(searchname, file=sys.stderr)
        searchresult = db.web.session.query(models.UserAuth).filter_by(name = searchname).all()
        # the search result is empty.  Why?
        print(searchresult, file=sys.stderr)
        return flask.render_template('content_search.html', searchresults = searchresult)
    else:
        return flask.render_template('content_search.html')
