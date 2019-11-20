import datetime as dt

import pyg.web
from pyg.web import models
from pyg.web import db

# new user module.  Factor out.
def sign_new_user(email, password, name):

    # check if the email is already present in the db
    q = db.web.session.query(models.UserAuth).filter_by(email = email)
    if db.web.session.query(q.exists()).scalar():
        return "crud_user_exists_err"
    else:
        newperson = models.Person(created=dt.datetime.now())
        newperson.auth = models.UserAuth(name=name, password=password, email=email)
        db.web.session.add(newperson)
        db.web.session.commit()
        return "crud_user_create_success"
        
