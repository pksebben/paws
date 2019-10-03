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

    #unsure if this should be Org or OrgMembership
    orgs = fields.Nested(Org, many=True)

    @post_load
    def make_person(self, data, **kwargs):
        pprint(data)
        return models.Person(**data)





"""
This next chunk of code is for testing purposes, and should be deleted post-integration
"""

from marshmallow import pprint

import datetime as dt


bill = models.Person(id = 1, created=dt.datetime.now())
# bill.auth = models.UserAuth(id=bill.id, name="bill", password="stealmydata")
# bill.profile = models.UserProfile(id=bill.id, about="I am the dumb", avatar="the last aribender", birthday="but its my birthday, baby!", location="someplace", email="bill@hotmail.com")
schema = Person()
result = schema.dump(bill)

models.Person(**{ 'created': datetime.datetime(2019, 9, 5, 15, 39, 57, 544092),
 'id': 1,
 'orgs': []})


load_result = schema.load(result)
print("this is the load result:")
pprint(load_result)
