from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Table,
    Text,
    DateTime,
    Date,
    Numeric,
    Boolean)
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine


"""
models.py
This is where all the db models (and, by ORM extension, the schema) are created / configured.
If things here seem broken, a good place to start is the "basic relationship patterns" section of the SQLAlchemy docs.

TODO:
- implement the declarative method for member-to-team IOT use the recommended pattern re: additional data on relational fields.
- Scrap all the flask_security nonsense.
"""


Base = declarative_base()

class MemberToTeam(Base):
    """This table connects members to teams and can define ownership"""
    
    __tablename__ = "member_to_team"
    
    member_id = Column(Integer, ForeignKey('member.id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('team.id'), primary_key=True)
    is_owner = Column(Boolean, nullable=False)
    joined_on = Column(Date)
    member = relationship("Member", back_populates="teams")
    team = relationship("Team", back_populates="members")

class Shelter(Base):
    """Shelter data"""
    
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    location = Column(String(80))
    about = Column(Text)

class Member(Base):
    """Member is the central table which ties all member data together."""

    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=False, nullable=False)
    handle = Column(String(80), unique=True)
    about = Column(Text)
    avatar_url = Column(String(80))
    birthday = Column(Date)
    location = Column(String(40))
    twitch_handle = Column(String(40))
    created = Column(DateTime, nullable=False)
    rank = Column(Integer, nullable=True)
    active = Column(Boolean, nullable=False) # for account deletion

    # Relationship Config
    auth = relationship(
        "Auth",
        back_populates="member",
        uselist=False)
    donations = relationship(
        "Donation",
        back_populates="member"
    )
    fundraisers = relationship(
        "Fundraiser",
        back_populates="member"
    )
    teams = relationship("MemberToTeam", back_populates="member")

    def __str__(self):
        return str(self.id)


class Auth(Base):
    """
    UserAuth is for "native" or username/password auth into pyg.
    Flask-Security is being mixed in here, as there are more shared fields natively.
    It may be necessary to factor those elements out to Member.  Revisit.
    """

    __tablename__ = 'auth'

    id = Column(
        Integer,
        ForeignKey("member.id"),
        primary_key=True)
    passhash = Column(String(80), unique=False, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    active = Column(Boolean)
    member = relationship("Member", uselist=False)

    def __str__(self):
        return str(self.id)

"""
Team model

TODO:
there's a bug in date_joined that returns None in the team profile page.  Check it out (perhaps a fixtures problem?)
"""
class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    date_joined = Column(Date, nullable=False)
    missionstatement = Column(Text, nullable=True)
    website = Column(Text, nullable=True)
    facebook_url = Column(Text, nullable=True)
    twitter_url = Column(Text, nullable=True)
    twitch_url = Column(Text, nullable=True)
    instagram_url = Column(Text, nullable=True)
    members = relationship("MemberToTeam", back_populates="team")
    fundraisers = relationship("Fundraiser", back_populates="team")

    def __str__(self):
        return self.name


class Donation(Base):
    __tablename__ = "donation"

    id = Column(Integer, primary_key=True)
    amount = Column(Numeric(asdecimal=False), nullable=False)
    donor_name = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    member_id = Column(Integer, ForeignKey("member.id"))
    member = relationship("Member", back_populates="donations")
    fundraiser_id = Column(Integer, ForeignKey("fundraiser.id"), nullable=True)
    fundraiser = relationship("Fundraiser", back_populates="donations")

    def __str__(self):
        return "$%.2f" % self.amount


class Fundraiser(Base):
    """having trouble figuring out what the structure of this is going to be, because it might be instantiated from multiple entities.
    possible solutions:
    - have a non-nullable foreign key for member (as a member will always be in some way responsible for creating these) and a nullable foreign key to team and shelter
    """
    __tablename__ = "fundraiser"

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    banner = Column(String(50))  # URL for static banner image
    about = Column(Text(convert_unicode=True))
    created = Column(DateTime, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    target_funds = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)

    member_id = Column(Integer, ForeignKey("member.id"), nullable=False)
    member = relationship("Member", back_populates="fundraisers")
    team_id = Column(Integer, ForeignKey("team.id"), nullable=True)
    team = relationship("Team", back_populates="fundraisers")
    donations = relationship("Donation", back_populates="fundraiser")

    def __str__(self):
        return self.name


class NewsArticle(Base):
    __tablename__ = "newsarticle"

    id = Column(Integer, primary_key=True)
    slug = Column(Text(convert_unicode=True), unique=True)
    headline = Column(Text(convert_unicode=True))
    author = Column(Text(convert_unicode=True))
    date = Column(DateTime, nullable=False)
    snippet = Column(Text(convert_unicode=True, length=250), nullable=False)
    body = Column(Text(convert_unicode=True))

    def __str__(self):
        return self.headline


class Route(Base):
    __tablename__ = "route"
    id = Column(String(80), primary_key=True)
    texts = relationship("Text", back_populates="route")

    def __str__(self):
        return str(self.id)


class Text(Base):
    __tablename__ = "text"

    route_id = Column(String(80), ForeignKey('route.id'), primary_key=True)
    slug = Column(String(32), primary_key=True)
    text = Column(Text(convert_unicode=True))
    route = relationship("Route", back_populates="texts")

    def __str__(self):
        return "{}".format(self.slug)
