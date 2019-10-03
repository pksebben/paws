from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine


Base = declarative_base()

org_membership_table = Table('org_membership', Base.metadata,
                             Column('user_id', Integer, ForeignKey('person.id')),
                             Column('org_id', Integer, ForeignKey('org.id'))
)

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

    
class UserAuth(Base):
    __tablename__ = 'user_auth'
    
    id = Column(Integer, ForeignKey("person.id"), primary_key=True)
    name = Column(String(80), unique=False, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    email = Column(String(80), unique=True, nullable=False)

    
class UserProfile(Base):
    __tablename__ = 'user_profile'
    
    id = Column(Integer, ForeignKey("person.id"), primary_key=True)
    about = Column(String(2500))
    avatar = Column(String(80))
    birthday = Column(String(12))
    location = Column(String(20))


class Org(Base):
    __tablename__ = 'org'
    
    id = Column(Integer, primary_key=True)
    # people = relationship(
    #     "Person",
    #     secondary="org_membership",
    #     back_populates="children"
    # )


# class OrgMembership(Base):
#     __tablename__ = 'org_membership'
    
#     orgid = Column(Integer, ForeignKey("org.id"), primary_key=True)
#     personid = Column(Integer, ForeignKey("person.id"), primary_key=True)


class Fundraiser(Base):
    __tablename__ = 'fundraiser'
    
    id = Column(Integer, primary_key=True)

    
class TestMe(Base):
    __tablename__ = "test_me"

    id = Column(Integer, primary_key=True)

engine = create_engine("postgresql://coffee:wildseven@localhost:5432/coffee")

Base.metadata.create_all(engine)
