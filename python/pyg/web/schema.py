import datetime

from marshmallow import Schema, fields, post_load, ValidationError

import models


class UserAuth(Schema):
    id = fields.Integer()
    name = fields.String()
    password = fields.String()


class UserProfile(Schema):
    id = fields.Integer()
    about = fields.String()
    avatar = fields.String()
    birthday = fields.String()
    location = fields.String()
    email = fields.String()

    
class Org(Schema):
    id = fields.Integer()

    
class Person(Schema):
    id = fields.Integer()
    created = fields.DateTime()
    auth = fields.Nested(UserAuth, required=False, allow_none=True, many=False)
    profile = fields.Nested(UserProfile, required=False, allow_none=True, many=False)

    orgs = fields.Nested(Org, many=True)

    @post_load
    def make_person(self, data, **kwargs):
        pprint(data)
        return models.Person(**data)


