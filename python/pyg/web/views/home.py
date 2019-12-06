import flask
from flask import render_template

bp = flask.Blueprint('home', __name__)


@bp.route('/')
def home():
    return render_template('content_home.html')
