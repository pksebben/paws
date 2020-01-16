import flask
import sys

from sqlalchemy import func, desc
from wtforms import Form, StringField, SubmitField, RadioField, validators

from pyg.web import db, models


"""
Search page
This is a combination search and sort view that is the single source of direct access to all team, fundraiser, member profiles.

This page, once complete, should have the following functions:
Search for or Browse
-Members
--who are streamers
--who are just members
--who own team pages
--who own shelters
-Shelters
-Teams
-Fundraisers
Order results by
-cash raised (members fundraisers teams)
-start/end dates (in the case of fundraisers)
-profile age (teams and shelters)
-members (fundraisers and teams)
-location (shelters)
-probably more, but it's late today and my brain is fried.

Behaviors
- Search by string should serve up everything that matches the string, but be reducible to teams / fundraisers / etc.
 - Search results should be split into multiple tables for each of the different classes of thing to search for, such as players and teams.

TODO:
- Basically everything.  There's a ton of awkward SQL necessary to perform the correct sorting on all of these so I haven't gotten terribly far yet.
 - Fundraisers should track their own donations.

FIGGERITOUT:
So what I want to do is to factor out some of the query logic and have a set of configurable fields that would show a few different things:
1 - Ranking should be it's own thing, kind of.  When performed, it would be best to have a function that applies those rankings to a data object that's accessed intuitively.

"""

class SearchForm(Form):
    querystring = StringField("Search")
    searchfor = RadioField("Search For", choices=[("all","all"),("players","players"),("teams","teams"),("fundraisers","fundraisers"),("shelters", "shelters")], default="all")
    submit = SubmitField("Submit")

bp = flask.Blueprint('search', __name__)

"""
Searching:
Next are defined a set of functions for fetching data from various tables based on the search string.

TODO: this next function needs to filter for streamers.  Do we want another search function for non-streamer members?
"""

# format the query to work with the 'like' filter from SQLAlchemy
def likestring(query):
    return '%' + query + '%'

def queryforplayers(query):
    return db.web.session.query(models.Member).filter(models.Member.handle.like(likestring(query)))

def queryforteams(query):
    return db.web.session.query(models.Team).filter(models.Team.name.like(likestring(query)))

def queryforfundraisers(query):
    return db.web.session.query(models.Fundraiser).filter(models.Fundraiser.name.like(likestring(query)))

def queryforshelters(query):
    return db.web.session.query(models.Shelter).filter(models.Shelter.name.like(likestring(query)))

# this selector allows for flexible querying based on the 'search type' radio selector
queryselector = {'players':queryforplayers,
            'teams':queryforteams,
            'fundraisers':queryforfundraisers,
            'shelters':queryforshelters}

@bp.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(flask.request.form)
    results = {}
    if flask.request.method == 'POST':

        querystring = form.querystring.data
        querytype = form.searchfor.data
        if querytype == "all":
            results["players"] = queryforplayers(querystring)
            results["teams"] = queryforteams(querystring)
            results["fundraisers"] = queryforfundraisers(querystring)
            results["shelters"] = queryforshelters(querystring)
        else:
            results[querytype] = queryselector[querytype](querystring)

        """
        this next query returns errytang, but only certain data from errytang,

        What I think we should do is move this function somewhere such that it will live in the db
        """
        donations = db.web.session.query( # create query object...
            models.Member.handle,         # ...give me a table with member handles...
            func.sum(models.Donation.amount).label('total') # ..and the sum of 
        ).join(models.Donation
               ).group_by(
            models.Member.handle).order_by(desc('total')).all()
        """What we get out of this is a ranked list of member names with donation totals, and no other data.  This should be factored out somehow."""
        ranked = enumerate(donations, start=1)


        
        return flask.render_template(
            'content_search.html', donations=ranked, form=form, results=results)
    else:
        results["players"] = queryforplayers("")
        results["teams"] = queryforteams("")
        results["fundraisers"] = queryforfundraisers("")
        results["shelters"] = queryforshelters("")
        return flask.render_template('content_search.html', form=form, results=results)
