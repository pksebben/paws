from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Table, Text, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine



Base = declarative_base()

org_membership_table = Table('org_membership', Base.metadata,
                             Column('user_id', Integer, ForeignKey('person.id')),
                             Column('org_id', Integer, ForeignKey('org.id'))
)


# The base class for persons that relate person data to other tables
class Person(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    created = Column(String, nullable=False)
    auth = relationship("UserAuth", backref=backref("person", uselist=False), uselist=False)
    profile = relationship("UserProfile", backref=backref("person", uselist=False), uselist=False)
    orgs = relationship(
        "Org",
        secondary="org_membership",
        backref="parents"
    )

    
# The auth data for persons
class UserAuth(Base):
    __tablename__ = 'user_auth'
    
    id = Column(Integer, ForeignKey("person.id"), primary_key=True, onupdate="cascade")
    name = Column(String(80), unique=False, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    email = Column(String(80), unique=True, nullable=False)


# All the personal data for a person.  Things that will be on their profile
class UserProfile(Base):
    __tablename__ = 'user_profile'
    
    id = Column(Integer, ForeignKey("person.id"), primary_key=True, onupdate="cascade")
    about = Column(String(2500))
    avatar = Column(String(80))
    birthday = Column(String(12))
    location = Column(String(20))

    
# A list of primary keys for organizations
class Org(Base):
    __tablename__ = 'org'
    
    id = Column(Integer, primary_key=True)
    # IAN: do we want these to be Date or DateTime?
    date_joined = Column(Date)
    auth = relationship("OrgAuth", backref=backref("org", uselist=False), uselist=False)
    profile = relationship("OrgProfile", backref=backref("org", uselist=False), uselist=False)
    
# IAN: Re: orgs and authentication.  See below.
# Org authentication.  We may want to structure this such that a particular user has edit privileges, instead of authenticating directly.  
class OrgAuth(Base):
    __tablename__='org_auth'

    id = Column(Integer, ForeignKey("org.id"), primary_key=True, onupdate="cascade")
    name = Column(String(80), unique=True, nullable= False)
    password= Column(String(40), unique=False, nullable=False)

# IAN: are we going to split up shelters / gaming orgs / etc?
# Profile information for orgs.
class OrgProfile(Base):
    __tablename__='org_profile'

    id = Column(Integer, ForeignKey("org.id"), primary_key=True, onupdate="cascade")
    missionstatement = Column(Text, nullable=True)
    location = Column(String(50), nullable=True, unique=False)
    # maybe these should live in their own table?
    website = Column(Text, nullable=True)
    facebook_link = Column(Text, nullable=True)
    twitter_link = Column(Text, nullable=True)
    twitch_link = Column(Text, nullable=True)
    instagram_link = Column(Text, nullable=True)

    
# Donations.  id / timestamp / fkeys / name for donating party
class Donation(Base):
    __tablename__ = "donation"

    id = Column(Integer, primary_key=True)
    donor_name = Column(String, nullable=False)
    created = Column(String, nullable=False)
    fundraiser_id = Column(Integer, ForeignKey("fundraiser.id"))
    fundraiser = relationship("Fundraiser", back_populates="donations")
    beneficiary_id = Column(Integer, ForeignKey("beneficiary.id"))
    beneficiary = relationship("Beneficiary", back_populates="donations")
    #the user field should be in here IOT track who gets credit for raising the fundage.

    
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

    
# Generic text dump for site content.  When ready, deprecate and replace with better scheme.    
class Text(Base):
    __tablename__ = "text"

    id = Column(Integer, primary_key=True)
    text = Column(Text(convert_unicode=True))

    
#TODO: Factor out the engine connection string, present here and in db.py
engine = create_engine("postgresql://coffee:wildseven@localhost:5432/coffee")

Base.metadata.create_all(engine)
