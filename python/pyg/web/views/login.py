import flask
from sqlalchemy.orm.exc import NoResultFound
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import bcrypt

from pyg.web import db, models


"""
Login page
This is probably going to change a little, as I think we want this to be a modal rather than it's own whole thing.

TODO:
- how are all these functions going to be handled when this is a modal, potentially present on multiple views?
"""


bp = flask.Blueprint('login', __name__)


class LoginForm(Form):
    email = StringField(
        "Email", [
            validators.InputRequired(), validators.Email("please input a valid email address")])
    password = PasswordField("Password", [validators.InputRequired()])


def login_user(email, password):
    try:
        user = db.web.session.query(
            models.Auth).filter_by(
            email=email).one()
        assert bcrypt.verify(password, user.passhash)
        flask.session['userid'] = user.id
        return flask.redirect('/')
    except (AssertionError, NoResultFound):
        return flask.render_template(
            "login.html", failure_text="bad credentials. please retry")


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(flask.request.form)
    if flask.request.method == 'POST' and form.validate():
        return login_user(
            form.email.data, form.password.data)
    else:
        return flask.render_template("login.html", form=form)
