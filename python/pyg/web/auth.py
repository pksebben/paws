from marshmallow import Schema, fields, post_load, ValidationError
from flask import session

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

import pyg.web
from pyg.web import db
from pyg.web import models


"""
Auth.py
This **should** be totally broken since implementing bcrypt, but login seems to work just fine still.

TODO:
- investigate this zombie module, potentially deprecate.  Maybe fix.
"""


class AuthError(Exception):
    pass


def user(email, password):
    """login a user and set flask.session['userid'] to that id"""

    try:
        userauth = db.web.session.query(
            models.Auth).filter_by(
            email=email).one()
        assert userauth.password == password
        session['userid'] = userauth.id
    except AssertionError as err:
        # log err?
        raise AuthError
    except IntegrityError as err:
        # log err.orig
        raise AuthError
