import sys

import flask
from oscar import flag
from flask_sqlalchemy import SQLAlchemy

import pyg.web
from pyg.web import api
from pyg.web import container

FLAGS = flag.namespace(__name__)
FLAGS.endpoint = flag.String("server endpoint" default=flag.REQUIRED)
FLAGS.debug = flag.Bool("enable debug", default=False)

app = flask.Flask(__name__)
    
# Do we want to put the database URI in a config file?
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://coffee:wildseven@localhost:5432/coffee"
db = SQLAlchemy(app)


class Person(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship("Userauth", "Userprofile", "Orgmembership")

    
class UserAuth(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    
class UserProfile(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
    about = db.Column(db.String(2500))
    avatar = db.Column(db.String(80))
    birthday = db.Column(db.String(12))
    location = db.Column(db.String(20))
    email = db.Column(db.String(30))


class Org(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship("Orgmembership")


class OrgMembership(db.Model):
    orgid = db.Column(db.Integer, db.ForeignKey("org.id"), primary_key=True)
    personid = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)


class Fundraiser(db.Model):
    id = db.Column(db.Integer, primary_key=True)


def create_app():
    # TODO: everything
    app.register_blueprint(api.bp)
    return app


def main():
    container.run(create_app(), FLAGS.endpoint, FLAGS.debug)

if __name__ == "__main__":
    flag.parse_commandline(sys.argv[1:])
    flag.die_on_missing_required()
    main()
