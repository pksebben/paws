import flask
import sys

from sqlalchemy import func, desc
from wtforms import Form, StringField, SubmitField, RadioField, validators

from pyg.web import db, models


from marshmallow import Schema, fields


class MemberSchema(Schema):
    handle = fields.Str()
    rank = fields.Integer()


"""
Search page
This is a combination search and sort view that is the single source of direct access to all team, fundraiser, member profiles.
TODO(kirby) : The dropdown for search disappears on focus.

TODO(ben): This module is a right mess.  Spend some time.

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

TODO(ben) : The search modal in the navbar should show "browse" button instead of "search" unless there is some input.  Also the modal dropdown should reflect this.
TODO(ben) : configure datatables for sensible defaults

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
TODO(design) : styling for datatables elements; see https://datatables.net/manual
TODO(ben) : format amounts raised
"""


def queryforplayers(query):
    results = db.web.session.query(models.Member).filter(
        models.Member.handle.like("%{}%".format(query))).all()
    json_results = []
    for i in results:
        json_results.append({
            "id": i.id,
            "handle": i.handle,
            "rank": i.rank,
            "raised": sum(y.amount for y in i.donations)
        })
    return json_results


def queryforteams(query):
    return db.web.session.query(models.Team).filter(
        models.Team.name.like("%{}%".format(query)))


def queryforfundraisers(query):
    return db.web.session.query(models.Fundraiser).filter(
        models.Fundraiser.name.like("%{}%".format(query)))


def queryforshelters(query):
    return db.web.session.query(models.Shelter).filter(
        models.Shelter.name.like("%{}%".format(query)))


# this selector allows for flexible querying based on the 'search type'
# radio selector
queryselector = {'players': queryforplayers,
                 'teams': queryforteams,
                 'fundraisers': queryforfundraisers,
                 'shelters': queryforshelters}


@bp.route('/search', methods=['GET', 'POST'])
@bp.route('/search/<sort_by>')
def search():
    form = SearchForm(flask.request.form)
    results = {"players": {},
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
