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
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin




"""
models.py
This is where all the db models (and, by ORM extension, the schema) are created / configured.
If things here seem broken, a good place to start is the "basic relationship patterns" section of the SQLAlchemy docs.

TODO:
- implement the declarative method for member-to-team IOT use the recommended pattern re: additional data on relational fields.
- Scrap all the flask_security nonsense.
"""


Base = declarative_base()


member_to_team = Table("member_to_team", Base.metadata,
                       Column('member_id', Integer, ForeignKey('member.id')),
                       Column('team_id', Integer, ForeignKey('team.id')),
                       Column('owner', Boolean, nullable=False)
                       )

roles_auths = Table("roles_auths", Base.metadata,
                    Column("auth_id", Integer, ForeignKey('auth.id')),
                    Column("role_id", Integer, ForeignKey('role.id'))
                    )


class Role(Base, RoleMixin):
    __tablename__ = 'role'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    desc = Column(String(255))


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
    teams = relationship("Team", secondary=member_to_team)

    def __str__(self):
        return str(self.id)


class Auth(Base, UserMixin):
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


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    date_joined = Column(Date)
    missionstatement = Column(Text, nullable=True)
    location = Column(String(50), nullable=True, unique=False)
    website = Column(Text, nullable=True)
    facebook_url = Column(Text, nullable=True)
    twitter_url = Column(Text, nullable=True)
    twitch_url = Column(Text, nullable=True)
    instagram_url = Column(Text, nullable=True)
    members = relationship("Member", secondary=member_to_team)
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
    datetime = Column(DateTime, nullable=False)
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
