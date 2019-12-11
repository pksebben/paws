import flask
import sys


from pyg.web import db, models

bp = flask.Blueprint('search', __name__)

class Player:
    def __init__(self, auth, profile):
        self.name = auth.name
        self.email = auth.email
        self.amountraised = 0
        # get all donations and add to amountraised
        donations = db.web.session.query(models.Donation).filter_by(person_id = auth.id).all()
        for i in donations:
            self.amountraised += i.amount
        # How are we going to calculate rank?
        

@bp.route('/search', methods=['GET', 'POST'])
def search():
    if flask.request.method == 'POST':
        searchname = flask.request.form['name']
        players = db.web.session.query(
            models.UserAuth).filter_by(
                name=searchname).all()
        teams = db.web.session.query(
            models.TeamAuth.filter_by(
                name=searchname.all()
            )
        )
        return flask.render_template(
            'content_search.html', players=players, teams=teams)
    else:

        return flask.render_template('content_search.html')
