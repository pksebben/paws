import random
import datetime

import flask
from flask import render_template
from sqlalchemy import desc, func

from pyg.web import models, db
from pyg.web.views.login import LoginForm
from pyg.web.views.leaderboard import rankedlist

# Goal: MVP grabbing: get the player on a team with the most raised
# (perhaps, this should be for that team).


def mvp():
    # THIS SHOULD BE DONE IN A SINGLE QUERY
    # member = db.web.session.query(models.Member.handle,
    #                               func.sum(
    # models.Donation.amount).label('total').join(
    #     models.Team).group_by(
    #         models.Member.handle).filter(models.Member.teams)
    
                                  
@bp.route('/sqltest')
def sqltest():
    
    team = db.web.session.query(models.Team).get(1)
    for i in team.members:
        
