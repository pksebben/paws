import datetime
import random
import string

import sqlalchemy
from sqlalchemy import orm
from passlib.hash import bcrypt

from pyg.web import models
from pyg.web import db


"""
fixtures.py
This is a module for populating testing data into the db.  It's used in two places:
1 - the test suite
2 - as a standalone, whenever the dev version of the site is being data wacky or you want to add new testing data.
"""


def lorem(n):
    return " ".join("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?""".split(
        " ")[0:n])


engine = None
session = None


def init():
    global engine
    global session
    engine = sqlalchemy.create_engine(db.FLAGS.web)
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)
    sessionmaker = orm.sessionmaker(bind=engine)
    session = sessionmaker()


def pick_member():
    members = session.query(models.Member).all()
    return random.choice(members)


def pick_team():
    teams = session.query(models.Team).all()
    return random.choice(teams)


def pick_fundraiser():
    fundraisers = session.query(models.Fundraiser).all()
    return random.choice(fundraisers)


def articles():
    article_1 = models.NewsArticle(
        headline=lorem(5),
        author=lorem(2),
        date=datetime.datetime.now(),
        body=lorem(-1),
        slug="article-1",
        snippet="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium."
    )
    session.add(article_1)

    article_2 = models.NewsArticle(
        headline=lorem(2),
        author=lorem(2),
        date=datetime.datetime.now(),
        body=lorem(-1),
        slug="article-2",
        snippet="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium."
    )
    session.add(article_2)

    session.commit()

# TODO: Factor out name generator.  Perhaps to it's own imported module.
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [i for i in string.ascii_lowercase if i not in vowels]


def makeaname(length):
    name = []
    name.append(random.choice(string.ascii_uppercase))
    for i in range(length):
        if name[-1].lower() == 'q':
            name.append('u')
        elif name[-1].lower() in vowels:
            name.append(random.choice(consonants))
        else:
            name.append(random.choice(vowels))
    return ''.join(name)


def garble(length):
    return "".join(random.choice(string.ascii_uppercase)
                   for i in range(length))


def generate_person():
    person = models.Member(
        name=makeaname(8),
        created=datetime.datetime.now(),
        handle=makeaname(8),
        about=garble(150),
        birthday=datetime.datetime.now(),
        location=garble(12),
        active=True,
        avatar_url="avatar_placeholder.jpg"
    )
    session.add(person)
    session.commit()


def crowd(numpeople):
    for i in range(numpeople):
        generate_person()


def people():
    tom = models.Member(
        name="tom",
        created=datetime.datetime.now(),
        handle="tom_dawg",
        about="my name is tom.  I am not good with about sections",
        birthday=datetime.datetime.now(),
        location="The town of hogsface, Land of foon",
        active=True,
        avatar_url="avatar_placeholder.jpg"
    )
    tom.auth = models.Auth(
        passhash=bcrypt.hash("pass"),
        email="tom@gmail.com"
    )
    othertom = models.Member(
        name="tom",
        created=datetime.datetime.now(),
        handle="tom_2",
        about="my name is other tom.  I am not good with about sections",
        birthday=datetime.datetime.now(),
        location="The town of hogsface, Land of foon",
        active=True,
        avatar_url="avatar_placeholder.jpg"
    )
    othertom.auth = models.Auth(
        passhash=bcrypt.hash("pass"),
        email="othertom@gmail.com"
    )
    bob = models.Member(
        name="bob",
        created=datetime.datetime.now(),
        handle="bob_the_builder",
        about="my name is bob.  I am not good with about sections",
        birthday=datetime.datetime.now(),
        location="The town of pigsface, Land of foon",
        active=True,
        avatar_url="avatar_placeholder.jpg"
    )
    bob.auth = models.Auth(
        passhash=bcrypt.hash("pass"),
        email="bob@gmail.com"
    )
    bill = models.Member(
        name="bill",
        created=datetime.datetime.now(),
        handle="boogie_2988",
        about="my name is bill.  I am not good with about sections",
        birthday=datetime.datetime.now(),
        location="The town of hogsface, Land of foon",
        active=True,
        avatar_url="avatar_placeholder.jpg"
    )
    bill.auth = models.Auth(
        passhash=bcrypt.hash("pass"),
        email="bill@gmail.com"
    )
    session.add(othertom)
    session.add(bill)
    session.add(tom)
    session.add(bob)
    session.commit()


def donations(numdonations):
    members = session.query(models.Member).all()
    for _ in range(numdonations):
        donation = models.Donation(member_id=random.choice(members).id,
                                   donor_name="Scroog McDuck",
                                   created=datetime.datetime.now(),
                                   amount=random.uniform(5, 100.01))
        session.add(donation)
    session.commit()


def text():
    home = models.Route(id="/")
    session.add(home)
    home_about_gamers = models.Text(
        route=home,
        slug="about_gamers",
        text="Participating gamers will be able to fundraise for the rescue of their choice while gaming for 24 hours straight."
    )
    session.add(home_about_gamers)
    home_about_funds = models.Text(
        route=home,
        slug="about_funds",
        text="We raise these funds in many ways, the primary source will be community gaming events and marathons."
    )
    session.add(home_about_funds)
    home_about_goal = models.Text(
        route=home,
        slug="about_goal",
        text="Our main goal is to provide funding for non-profit, no-kill animal rescues and refugees that will allow fosters and facilities to rescue more animals than ever before."
    )
    session.add(home_about_goal)
    home_intro_join = models.Text(
        route=home,
        slug="intro_join",
        text="Do you represent a no kill shelter? Interested in working or partnering with us? Sign up to learn more today on how you can help and support Paws Your Game."
    )
    session.add(home_intro_join)
    home_intro_start_gaming = models.Text(
        route=home,
        slug="intro_start_gaming",
        text="Love playing games? Love animals? Sign up to Paws Your Game and sponsor a local no kill shelter of your choice when we have our first marathon in 2019!"
    )
    session.add(home_intro_start_gaming)
    home_intro_donate = models.Text(
        route=home,
        slug="intro_donate",
        text="Want to help support Paws Your Game’s mission in providing resources to no kill shelters? Donate today to help support us in our mission to end kill shelters."
    )
    session.add(home_intro_donate)
    home_subtitle_header = models.Text(
        route=home,
        slug="subheader",
        text="Play Games for those without a voice"
    )
    session.add(home_subtitle_header)
    home_subtitle = models.Text(
        route=home,
        slug="subtitle",
        text="Paws Your Game’s mission is to help raise money and other resources for animal rescue organizations through video game marathons.")
    session.add(home_subtitle)
    session.commit()


def fundraisers():
    forthehorde = models.Fundraiser(
        name="Glory to the Horde fundraiser",
        about="The pillagers of azeroth are raising money for the fostering and care of orphaned Tauren.  These poor creatures have been left by their owners and have nowhere to turn.  Won't you help us to bring love and care to these cute little unfortunates? -cue sarah mcglaughlin- ",
        member=pick_member(),
        created=datetime.datetime.now(),
        start_date=datetime.datetime.now(),

        end_date=datetime.datetime(3000, 1, 1),
        target_funds=250
    )
    session.add(forthehorde)
    springbreak = models.Fundraiser(
        name="chads spring break fundraiser",
        about="what's all this nerd shit?  who plays videogames anyway and why are they all talking about having paws?  Is this some kind of furry convention?  Anyway, my bro brad said I could like, get money here or something, and if we get more fundage, we can get more lit!  You know what I mean?  Yeah, you know what I mean, loser!  Let's paaaaartay like it's like, hey, when did they party really hard?  was that the 70s?  Doesn't matter cause with all the money I'm gonna have I'm sure to get it in! Crush puss like I crush those miller lites yaknow!",
        member=pick_member(),
        created=datetime.datetime.now(),
        start_date=datetime.datetime(1985, 1, 1),
        end_date=datetime.datetime(2069, 1, 1),
        target_funds=5000000
    )
    session.add(springbreak)
    tomsfundraiser = models.Fundraiser(
        name="Tom is raising the funds",
        about="I am tom.  I like money",
        member=session.query(
            models.Auth).filter_by(
            email="tom@gmail.com").first().member,
        created=datetime.datetime.now(),
        start_date=datetime.datetime(2, 1, 1),
        end_date=datetime.datetime(3000, 1, 1),
        target_funds=250,
    )
    session.commit()


def create_team(owner, name):
    """all the things that teams start with, including an owner"""
    team = models.Team(name=name, date_created=datetime.datetime.now())
    relation = models.MemberToTeam(is_owner=True, joined_on=datetime.datetime.now())
    relation.member = owner
    team.members[relation.member.id] = relation
    session.add(team)
    session.commit()

def teams():
    tom = session.query(models.Auth).filter(models.Auth.email == "tom@gmail.com").one().member
    create_team(tom, "tom's team")

def shelters():
    shelter1 = models.Shelter(
        name="big bob's discount doggos",
        location="pittsburgh"
    )
    session.add(shelter1)
    session.commit()
    pass


def add_donations_to_fundraisers():
    donations = session.query(models.Donation).all()
    for i in donations:
        i.fundraiser = pick_fundraiser()
    session.commit()


def add_fundraisers_to_teams():
    fundraisers = session.query(models.Fundraiser).all()
    for i in fundraisers:
        i.team = pick_team()
    session.commit()


def gogogadget():
    init()
    articles()
    people()
    crowd(50)
    donations(500)
    text()
    fundraisers()
    teams()
    shelters()
    add_donations_to_fundraisers()
    add_fundraisers_to_teams()


if __name__ == "__main__":
    gogogadget()
