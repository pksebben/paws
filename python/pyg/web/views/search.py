import flask
import sys

from sqlalchemy import func, desc
from wtforms import Form, StringField, SubmitField, RadioField, validators

from pyg.web import db, models


"""
Search page
This is a combination search and sort view that is the single source of direct access to all team, fundraiser, member profiles.

TODO(ben): implement following
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
 - Sorting is becoming a bit of a monster. See note below

SORTING
Jinja has a sort filter, using it in it's raw form:
{% thingtosort|sort(attribute="attributetosort") %}
I want to tie this to an onclick
perhaps also to rerender the page?

I think turning this into a macro and then tying that to a click is the way

It seems like getting the page to rerender might be a bit of a hassle. I don't know what to do about this.
"""


class SearchForm(Form):
    querystring = StringField("Search")
    searchfor = RadioField(
        "Search For",
        choices=[
            ("all",
             "all"),
            ("players",
             "players"),
            ("teams",
             "teams"),
            ("fundraisers",
             "fundraisers"),
            ("shelters",
             "shelters")],
        default="all")
    submit = SubmitField("search")


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
    return db.web.session.query(models.Member).filter(
        models.Member.handle.like(likestring(query)))


def queryforteams(query):
    return db.web.session.query(models.Team).filter(
        models.Team.name.like(likestring(query)))


def queryforfundraisers(query):
    return db.web.session.query(models.Fundraiser).filter(
        models.Fundraiser.name.like(likestring(query)))


def queryforshelters(query):
    return db.web.session.query(models.Shelter).filter(
        models.Shelter.name.like(likestring(query)))


# this selector allows for flexible querying based on the 'search type'
# radio selector
queryselector = {'players': queryforplayers,
                 'teams': queryforteams,
                 'fundraisers': queryforfundraisers,
                 'shelters': queryforshelters}


@bp.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(flask.request.form)
    results = {"players": [],
               "teams": [],
               "fundraisers": [],
               "shelters": []}
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

        return flask.render_template(
            'content_search.html', form=form, results=results, sortby="id")
    else:
        results["players"] = queryforplayers("")
        results["teams"] = queryforteams("")
        results["fundraisers"] = queryforfundraisers("")
        results["shelters"] = queryforshelters("")
        return flask.render_template(
            'content_search.html', form=form, results=results, sortby="id")
