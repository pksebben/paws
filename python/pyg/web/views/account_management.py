import sys

import flask
from wtforms import Form, StringField, validators
from passlib.hash import bcrypt

from pyg.web import db, models


"""
Account Management page.
Allows users to do things like change passwords, delete their account, that kinda junk.  An extra layer of distance over the profile editing page for functions that are potentially hazardous.

TODO:
- account deletion
- add validators to the change pass form
- have a conversation about what else should go in here.
- have a brief conversation about whether there should be an extra layer of security over this module, as it concerns the changing and recovery of passwords
- should the change password function be factored out?  Maybe a modal?

"""

bp = flask.Blueprint("account_management", __name__)

# TODO: add validators
class ChangePasswordForm(Form):
    oldpassword = StringField("Old Password")
    newpassword = StringField("New Password", validators=[validators.EqualTo(newpasswordconfirm)])
    newpasswordconfirm = StringField("Confirm New Password")


def changepassword(memberid, oldpass, newpass):
    member = db.web.session.query(models.Member).get(memberid)
    if member.id == flask.session['userid']:
        if bcrypt.verify(oldpass, member.auth.passhash):
            member.auth.passhash = bcrypt.hash(newpass)
            return True
        else:
            print("old password mismatch", file=sys.stderr)
            return False
    else:
        print("logged in user mismatch", file=sys.stderr)
        return False


@bp.route('/account/<memberid>', methods=["POST", "GET"])
def accountmanagement(memberid):
    member = db.web.session.query(models.Member).get(memberid)
    auth = member.auth
    passform = ChangePasswordForm(flask.request.form)
    if flask.request.method == "POST" and passform.validate():
        if changepassword(memberid, passform.oldpassword.data,
                          passform.newpassword.data):
            flask.flash("password successfully changed!")
            return flask.render_template(
                "account_management.html", passform=passform, member=member, auth=auth)
        else:
            flask.flash("faulty information provided. Please try again.")
            return flask.render_template(
                "account_management.html", passform=passform, member=member, auth=auth)
    else:
        # Is this secure enough?  Should we implement some form of security
        # validation?
        if flask.session['userid'] == member.id:
            return flask.render_template(
                "account_management.html", passform=passform, member=member, auth=auth)
        else:
            return flask.render_template("errorpage.html")
