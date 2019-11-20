import datetime as dt

import pyg.web
from pyg.web import models
from pyg.web import db


# create a new user.  Takes dict as input
def create_new_person(person):

    print('creating new person')
    checkexists = db.web.session.query(models.UserAuth).filter_by(email=person['email'])
    checkexists = list(checkexists)

    if checkexists:
        print("user exists already")
        pass
    else:
        print("attempting to create new user")
        newperson = models.Person(created=dt.datetime.now())
        newperson.auth = models.UserAuth(name=person['name'], password=person['password'],email=person['email'])
        newperson.profile=models.UserProfile(about=person['about'], avatar=person['avatar'], birthday=person['birthday'], location=person['location'])
        db.web.session.add(newperson)
        db.web.session.commit()
        print("user entered successfully")


def populate():
    print("calling populate")
    tom = { 'name':'tom', 'password':'pass', 'email':'tom@gmail.com', 'about':'My name is tom.', 'avatar':'', 'birthday':'every day', 'location':'New Jersey'}
    create_new_person(tom)
    print("Database populated")
