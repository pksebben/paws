import datetime as dt
import sys

from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

import pyg.web
from pyg.web import models
from pyg.web import db
from pyg.web import views


# TODO: this should be implementing the same user creation in views.
# create a new user.  Takes dict as input
def create_new_person(person):
    
    try:
        views.sign_new_user(name=person['name'], email=person['email'], password=person['password'])
        pass
    except IntegrityError as err:
        print(err.orig)
        db.web.session.rollback()
        pass
    
    try:
        print("adding profile")
        user = db.web.session.query(models.UserAuth).filter_by(email=person['email']).one().person
        print("to user")
        print(user)
        views.update_user_profile(id=user.id,
                                about=person['about'],
                                birthday=person['birthday'],
                                location=person['location'])
    except:
        raise

def populate():
    print("calling populate")
    tom = { 'name':'tom', 'password':'pass', 'email':'tom@gmail.com', 'about':'My name is tom.', 'avatar':'', 'birthday':dt.datetime.now(), 'location':'New Jersey'}
    create_new_person(tom)
    print("Database populated")
