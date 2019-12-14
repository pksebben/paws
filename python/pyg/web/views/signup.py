import datetime as dt

import flask
from flask import render_template, flash, request, redirect
from sqlalchemy.exc import IntegrityError

from pyg.web import models
from pyg.web import db
from pyg.web import auth


bp = flask.Blueprint('signup', __name__)


def sign_new_user(email, password, name):
    try:
        newperson = models.Member(created=dt.datetime.now(), name=name)
        newperson.auth = models.Auth(
            password=password, email=email)
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
    if request.method == "POST":
        try:
            email = request.form['email']
            password = request.form['password']
            name = request.form['name']
            sign_new_user(email, password, name)
            auth.user(email, password)
            return redirect('/')
        except IntegrityError as err:
            flash("we found a user with that email already.")
            return render_template('signup.html')
    else:
        return render_template('signup.html')
