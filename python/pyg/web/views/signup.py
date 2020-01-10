import datetime as dt

import flask
from flask import render_template, flash, request, redirect
from sqlalchemy.exc import IntegrityError
from wtforms import Form, validators, StringField, PasswordField
from passlib.hash import bcrypt

from pyg.web import models
from pyg.web import db
from pyg.web import auth


"""
Member Signup page
This is where members create their profile.  Most of the actual profile data lives in their profile and can be modified there once they are logged in; this should just have them set the non-nullable points of data like password and email and such.

It shouldn't need to be said, so I'll say it: anything dealing with passwords should use encryption.

TODO:
- figure out a workflow re: nullable emails once Oauth becomes a thing.
- Configure bcrypt to use random salts
"""

bp = flask.Blueprint('signup', __name__)


class RegistrationForm(Form):
    email = StringField("Email", [validators.InputRequired(
    ), validators.Email("please input a valid email address")])
    name = StringField("Name", [validators.InputRequired()])
    password = PasswordField("Password",
                             [validators.InputRequired(),
                              validators.EqualTo("password_confirm"),
                                 validators.length(min=12)])
    password_confirm = PasswordField("Confirm Password")


def sign_new_user(email, password, name):
    try:
        newperson = models.Member(created=dt.datetime.now(), name=name)
        passhash = bcrypt.hash(password)
        newperson.auth = models.Auth(
            passhash=passhash, email=email)
        db.web.session.add(newperson)
        db.web.session.commit()
        return newperson.id
        # change to structlog
        # print("user created")
    except IntegrityError as err:
        db.web.session.rollback()
        raise err


@bp.route('/signup', methods=['POST', 'GET'])
def home():
    form = RegistrationForm(flask.request.form)
    if request.method == "POST" and form.validate():
        try:
            sign_new_user(form.email.data, form.password.data, form.name.data)
            auth.user(form.email.data, form.password.data)
            return redirect('/')
        except IntegrityError as err:
            flash("we found a user with that email already.")
            return render_template('signup.html', form=form)
    else:
        return render_template('signup.html', form=form)
