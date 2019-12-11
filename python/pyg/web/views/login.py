import flask
from sqlalchemy.orm.exc import NoResultFound

from pyg.web import db, models

bp = flask.Blueprint('login', __name__)


def login_user(email, password):
    try:
        user = db.web.session.query(
            models.UserAuth).filter_by(
            email=email).one()
        assert user.password == password
        flask.session['userid'] = user.id
        return flask.redirect('/')
    except (AssertionError, NoResultFound):
        return flask.render_template(
            "login.html", failure_text="bad credentials. please retry")


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        return login_user(
            flask.request.form['email'], flask.request.form['password'])
    else:
        return flask.render_template("login.html")
