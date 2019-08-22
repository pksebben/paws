from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    auth = relationship("UserAuth", backref="person")
    profile = relationship("UserProfile", backref="person")
    orgs = relationship(
        "Org",
        secondary="org_membership"                
    )

    
class UserAuth(Base):
    __tablename__ = 'user_auth'
    
    id = Column(Integer, ForeignKey("person.id"), primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)

    
class UserProfile(Base):
    __tablename__ = 'user_profile'
    
    id = Column(Integer, ForeignKey("person.id"), primary_key=True)
    about = Column(String(2500))
    avatar = Column(String(80))
    birthday = Column(String(12))
    location = Column(String(20))
    email = Column(String(30))


class Org(Base):
    __tablename__ = 'org'
    
    id = Column(Integer, primary_key=True)
    people = relationship(
        "Person",
        secondary="org_membership"
    )


class OrgMembership(Base):
    __tablename__ = 'org_membership'
    
    orgid = Column(Integer, ForeignKey("org.id"), primary_key=True)
    personid = Column(Integer, ForeignKey("person.id"), primary_key=True)


class Fundraiser(Base):
    __tablename__ = 'fundraiser'
    
    id = Column(Integer, primary_key=True)

    
class TestMe(Base):
    __tablename__ = "test_me"

    id = Column(Integer, primary_key=True)
