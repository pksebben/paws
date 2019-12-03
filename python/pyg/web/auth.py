from marshmallow import Schema, fields, post_load, ValidationError
from flask import session

# from psycopg2.errors import 
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

import pyg.web
from pyg.web import db
from pyg.web import models


class AuthError(Exception):
    pass

# TODO: implement hashing and better password management
# Log in a user.  If successful, sets a flask session variable
def user(email, password):

    try:
        userauth = db.web.session.query(models.UserAuth).filter_by(email=email).one()
        assert userauth.password == password
        session['userid'] = userauth.id
    except AssertionError as err:
        # log err?
        raise AuthError
    except IntegrityError as err:
        # log err.orig
        raise AuthError
