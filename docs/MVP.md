#MVP Production Targets
This document is meant to track progress on the minimum viable product release of PyG.  The aim is to have this live by the end of August 2019

This is meant to be a living document.  Tasks and targets will be written here in the most basic of formats, and then should be fleshed out as planning goes on.  Once a feature has been completed, mark it as such.  If there are notes on the development of a feature, they can live here or in the documentation in the source code for that feature.  Once complete, all dev notes should be moved to either
*this document
*another document in this folder.

##Overview

###Features
These are the features necessary for release of 1.0.

*Database
   *Usertable
      *Primary Keys
   *User Auth
      *Password
      *Name
   *Org table
      *NEEDS SCHEMA
   *Org membership
      *NEEDS SCHEMA
   *Profile Table
      *NEEDS SCHEMA
   *Rescue Table
      *NEEDS SCHEMA
*Pages
   *Home
   *User Profile
   *Shelter Profile
   *Login
   *About
   *Adoption Page

###Tech Stack
This is the stack we're implementing.

####Frontend

#####React
#####Redux

####Backend

#####SQLAlchemy
#####PostgresSQL
#####Flask
#####Ansible
#####Google Cloud Platform




GOALS
########################
Database goals
~~~~~~~~~~~~~~~~~~~~~~~~~
Design a usertable
primary key - auto-increment / uniqueness constraint

Design a table for user password / username
Primary key (foriegn keyed to usertable)
username
password

Organization table
{shelters / teams / rescues / etc.}

Table for org membership / admin
{links two primary keys together to link users to orgs}

Profile table
{keeps bio info and website and twitter and such data keyed to users}

Rescue table
{keeps adoption data for the adoption page}

Page goals
~~~~~~~~~~~~~~~~~~~~~~~~
Login
Home
User profile
Shelter profile
About
Adoption page
