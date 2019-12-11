from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Table, Text, DateTime, Date
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
    auth = relationship(
        "Auth",
        backref=backref(
            "member",
            uselist=False),
        uselist=False)
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


class Auth(Base):
    """UserAuth is for "native" or username/password auth into pyg."""

    __tablename__ = 'auth'

    id = Column(
        Integer,
        ForeignKey("member.id"),
        primary_key=True,
        onupdate="cascade")
    name = Column(String(80), unique=False, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    email = Column(String(80), unique=True, nullable=False)


class Profile(Base):
    """Profile is member specifics."""

    __tablename__ = 'profile'

    id = Column(
        Integer,
        ForeignKey("member.id"),
        primary_key=True,
        onupdate="cascade")
    about = Column(Text)
    avatar_url = Column(String(80))
    birthday = Column(Date)
    location = Column(String(40))
    twitch_handle = Column(String(40))


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    date_joined = Column(Date)
    missionstatement = Column(Text, nullable=True)
    location = Column(String(50), nullable=True, unique=False)
    website = Column(Text, nullable=True)
    facebook_url = Column(Text, nullable=True)
    twitter_url = Column(Text, nullable=True)
    twitch_url = Column(Text, nullable=True)
    instagram_url = Column(Text, nullable=True)
    members = relationship("Member", secondary=member_to_team)


class Donation(Base):
    __tablename__ = "donation"

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    donor_name = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    fundraiser_id = Column(Integer, ForeignKey("fundraiser.id"))
    fundraiser = relationship("Fundraiser", back_populates="donations")
    beneficiary_id = Column(Integer, ForeignKey("beneficiary.id"))
    beneficiary = relationship("Beneficiary", back_populates="donations")
    member_id = Column(Integer, ForeignKey("member.id"))
    member = relationship("Member", back_populates="donations")


# #This seems like it might be better kept as a table of NGOs or something of that nature.
class Beneficiary(Base):
    __tablename__ = "beneficiary"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    donations = relationship("Donation")


# Primary keys for fundraisers
class Fundraiser(Base):
    __tablename__ = 'fundraiser'

    id = Column(Integer, primary_key=True)
    donations = relationship("Donation")


"""
######################### MISC DATA #########################
-refactor into actual data for prod.
"""


class NewsArticle(Base):
    __tablename__ = "newsarticle"

    id = Column(Integer, primary_key=True)
    slug = Column(Text(convert_unicode=True), unique=True)
    headline = Column(Text(convert_unicode=True))
    author = Column(Text(convert_unicode=True))
    datetime = Column(DateTime, nullable=False)
    body = Column(Text(convert_unicode=True))


# Generic text dump for site content.  When ready, deprecate and replace
# with better scheme.
class Text(Base):
    __tablename__ = "text"

    id = Column(Integer, primary_key=True)
    text = Column(Text(convert_unicode=True))
