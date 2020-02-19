import flask


"""
Account Deleted page

This just serves a notification that account deletion has been successful.

TODO(ian): read the rest of this docstring
Deletion mechanics are a thing that I've looked at and have been stumped by.  I know ways to get this done, but there are problems with all of them and I need an opinion on what to do.

OPTIONS:

#1 Make a seperate table for deleted members, move records there and cut all relationships
PRO: Doesn't break any other parts of the site, quick implementation, maintains data
CON: It just feels wrong, and I anticipate problems with related objects, and I feel like it would violate some things that you said not to do with databases but I can't remember what they are

#2 Set a boolean on the model that tracks whether deleted
PRO: simple implementation, maintains data
CON: This is going to require that _every place we use member in a query_ get changed.  Some of these will take forever to do, as they are queries for related data that use a member id to look at.  I really don't want to do this one.

#3 Delete the record
PRO: fairly straightforward implementation
CON: trashes the data (non-rollbackable), also, see option #1 - this will give us the same relational headaches etc

#4 ????
I'm assuming there's a good way to do this but the internet has a lot of wrong opinions and I'm at a loss.

"""

bp = flask.Blueprint("account_deleted", __name__)


@bp.route('/account_deleted')
def account_deleted():
    return flask.render_template("account_deleted.html")
