from marshmallow import Schema, fields, post_load, ValidationError
from flask import session

# from psycopg2.errors import 
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

import pyg.web
from pyg.web import db
from pyg.web import models
from pyg.web.exceptions import PasswordError, UserNotFoundError



"""Auth.  This could, potentially, be merged with api.  I figured, however that it would likely grow quite a bit once Oauth is implemented."""

# Log in a user.  If successful, sets a flask session variable
def user(email, password):
    
    class AuthSchema(Schema):
        email = fields.String()
        password = fields.String()

    class PersonSchema(Schema):
        id = fields.Integer()
        auth = fields.Nested(AuthSchema, required=True, allow_none=False, many=False)



    try:
        userauth = db.web.session.query(models.UserAuth).filter_by(email=email).one()
        assert userauth.password == password
        session['userid'] = userauth.id
    except AssertionError:
        print("password mismatch")
        raise PasswordError
    except IntegrityError as err:
        raise err.orig
    except NoResultFound as err:
        print("No user found to authorize")
        raise UserNotFoundError
        

