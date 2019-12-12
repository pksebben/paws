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
    Numeric)
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine


Base = declarative_base()


member_to_team = Table("member_to_team", Base.metadata,
                       Column('member_id', Integer, ForeignKey('member.id')),
                       Column('team_id', Integer, ForeignKey('team.id')))


class Member(Base):
    """Member is the central table which ties all member data together."""

    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    auth = relationship("Auth", uselist=False)
    profile = relationship(
        "Profile",
        backref=backref(
            "member",
            uselist=False),
        uselist=False)
    donations = relationship(
        "Donation",
        back_populates="member"
    )
    teams = relationship("Team", secondary=member_to_team)

    def __str__(self):
        return str(self.id)


class Auth(Base):
    """UserAuth is for "native" or username/password auth into pyg."""

    __tablename__ = 'auth'

    id = Column(
        Integer,
        ForeignKey("member.id"),
        primary_key=True)
    name = Column(String(80), unique=False, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    member = relationship("Member", uselist=False)

    def __str__(self):
        return str(self.id)


class Profile(Base):
    """Profile is member specifics."""

    __tablename__ = 'profile'

    id = Column(
        Integer,
        ForeignKey("member.id"),
        primary_key=True)
    handle = Column(String(80), unique=True)
    about = Column(Text)
    avatar_url = Column(String(80))
    birthday = Column(Date)
    location = Column(String(40))
    twitch_handle = Column(String(40))

    def __str__(self):
        return self.handle


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

    def __str__(self):
        return "$%.2f" % self.amount


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
