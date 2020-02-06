import random
import datetime

import flask
from flask import render_template
from sqlalchemy import desc, func

from pyg.web import models, db
from pyg.web.views.login import LoginForm
from pyg.web.views.leaderboard import rankedlist


@bp.route('/sqltest')
def sqltest():
    
