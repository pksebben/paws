from marshmallow import Schema, fields, post_load, ValidationError
from flask import session

import pyg.web
from pyg.web import db
from pyg.web import models



def user(email, password):
#get email and password from request
    
    class AuthSchema(Schema):
        email = fields.String()
        password = fields.String()

    class PersonSchema(Schema):
        id = fields.Integer()
        auth = fields.Nested(AuthSchema, required=True, allow_none=False, many=False)

    #get the id of the user being logged in
    userauth = db.web.session.query(models.UserAuth).filter_by(email=email)

    q = list(userauth)

    print("###USERAUTH###")
    print(userauth)
    print("###LIST OF USERAUTH###")
    print(q)

    #did we find a user auth?
    if q:
        user = q[0].person
        #do the login shuffle
        #does the password match?
        if q[0].password == password:
            session['userid'] = q[0].id
            return "auth_success"
            #TODO: send the user id# so the client just knows who's using it.
        else:
            return "auth_pass_err"
    else:
        return "auth_email_err"
