import datetime as dt

import pyg.web
from pyg.web import models
from pyg.web import db



def sign_new_user(email, password, name):

    newperson = models.Person(created=dt.datetime.now())
    newperson.auth = models.UserAuth(name=name, password=password, email=email)
    db.web.session.add(newperson)
    db.web.session.commit()
    print("user created")

def update_user_profile(id, about, birthday, location):
    user = db.web.session.query(models.Person).get(id)
    if not user.profile:
        user.profile = models.UserProfile(about=about, birthday=birthday, location=location)
        print('added user profile')
    else:
        user.profile.about = about
        user.profile.birthday = birthday
        user.profile.location = location
        print('updated user profile')
    db.web.session.commit()
    print("user updated")
