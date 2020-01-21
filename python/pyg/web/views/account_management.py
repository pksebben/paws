import sys

import flask
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, validators
from passlib.hash import bcrypt

from pyg.web import db, models


"""
Account Management page.
Allows users to do things like change passwords, delete their account, that kinda junk.  An extra layer of distance over the profile editing page for functions that are potentially hazardous.

##ON HOLD##
Design decisions need to be made re: account deletion

TODO:
- account deletion mechanics
- have a conversation about what else should go in here.
- have a brief conversation about whether there should be an extra layer of security over this module, as it concerns the changing and recovery of passwords
- should the change password function be factored out?  Maybe a modal?
- implement better bad credential handling in changepassword()

++++
So this has become a bit of a mess trying to get two forms in there to work in tandem, but it's working so far.
FIXME:
- factor out the pasta
- get the validators working so they don't get called on both submits (this may have to do with the fact that both submit buttons are given the same ID, start by prefixing each form)
- There should be behaviors that make more sense upon account deletion / password change
- account deletion does not yet delete anything.
"""

bp = flask.Blueprint("account_management", __name__)


class ChangePasswordForm(Form):
    oldpassword = PasswordField("Old Password")
    newpassword = PasswordField(
        "New Password",
        validators=[
            validators.Length(min=12, message="must be at least 12 characters")])
    newpasswordconfirm = PasswordField(
        "Confirm New Password", validators=[
            validators.EqualTo('newpassword', message="password mismatch")])
    submit = SubmitField("Submit")

    # def validate(self):
    #     print("change password validation attempt")
    #     super(ChangePasswordForm, self).validate()


class DeleteAccountForm(Form):
    confirmdelete = BooleanField(
        "Delete my account", validators=[
            validators.DataRequired()])
    submit = SubmitField("Do it")

#     def validate(self):
#         print("delete account validation attempt")
#         super(DeleteAccountForm, self).validate()


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
    deleteform = DeleteAccountForm(flask.request.form)
    def showpage():
        return flask.render_template("account_management.html", passform=passform, deleteform=deleteform)
    if flask.request.method == "POST":
        if passform.submit.data and passform.validate():
                if changepassword(memberid, passform.oldpassword.data, passform.newpassword.data):
                    flask.flash("password changed")
                    return showpage()
                else:
                    flask.flash("incorrect credentials entered")
                    return showpage()
        elif deleteform.submit.data and deleteform.validate():
                print("BALEEEETED!!!!!!")
                """
                The function for deleting members needs to wait on a design decision re: how
                to handle deleting members.
                """
                # db.web.session.delete(member)
                # db.web.session.delete(auth)
                # db.web.session.commit()
                return flask.redirect('/account_deleted')
        else:
            return flask.render_template("errorpage.html")
    else:
        # Is this secure enough?  Should we implement some form of security
        # validation?
        if flask.session['userid'] == member.id:
            return flask.render_template(
                "account_management.html", passform=passform, deleteform=deleteform)
        else:
            return flask.render_template("errorpage.html")
