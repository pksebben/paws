import datetime
import random

import sqlalchemy
from sqlalchemy import orm

from pyg.web import models
from pyg.web import db


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


def articles():
    article_1 = models.NewsArticle(
        headline=lorem(5),
        author=lorem(2),
        datetime=datetime.datetime.now(),
        body=lorem(-1),
        slug="article-1")
    session.add(article_1)

    article_2 = models.NewsArticle(
        headline=lorem(2),
        author=lorem(2),
        datetime=datetime.datetime.now(),
        body=lorem(-1),
        slug="article-2")
    session.add(article_2)

    session.commit()


def people():
    tom = models.Member(
        created=datetime.datetime.now()
    )
    tom.auth = models.Auth(
        name="tom",
        password="pass",
        email="tom@gmail.com"
    )
    tom.profile = models.Profile(
        handle="tom_dawg",
        about="my name is tom.  I am not good with about sections",
        birthday=datetime.datetime.now(),
        location="The town of hogsface, Land of foon"
    )
    othertom = models.Member(
        created=datetime.datetime.now()
    )
    othertom.auth = models.Auth(
        name="tom",
        password="pass",
        email="othertom@gmail.com"
    )
    othertom.profile = models.Profile(
        handle="tom_2",
        about="my name is other tom.  I am not good with about sections",
        birthday=datetime.datetime.now(),
        location="The town of hogsface, Land of foon"
    )
    bob = models.Member(
        created=datetime.datetime.now()
    )
    bob.auth = models.Auth(
        name="bob",
        password="pass",
        email="bob@gmail.com"
    )
    bob.profile = models.Profile(
        handle="bob_the_builder",
        about="my name is bob.  I am not good with about sections",
        birthday=datetime.datetime.now(),
        location="The town of pigsface, Land of foon"
    )
    bill = models.Member(
        created=datetime.datetime.now()
    )
    bill.auth = models.Auth(
        name="bill",
        password="pass",
        email="bill@gmail.com"
    )
    bill.profile = models.Profile(
        handle="boogie_2988",
        about="my name is bill.  I am not good with about sections",
        birthday=datetime.datetime.now(),
        location="The town of hogsface, Land of foon"
    )
    session.add(othertom)
    session.add(bill)
    session.add(tom)
    session.add(bob)
    session.commit()


def donations():
    members = session.query(models.Member).all()
    for _ in range(90):
        donation = models.Donation(member_id=random.choice(members).id,
                                   donor_name="Scroog McDuck",
                                   created=datetime.datetime.now(),
                                   amount=random.uniform(5, 100.01))
        session.add(donation)
    session.commit()


def text():
    home = models.Route(id="/")
    session.add(home)
    home_subtitle = models.Text(
        route=home,
        slug="subtitle",
        text="Paws Your Game’s mission is to help raise money and other resources for animal rescue organizations through video game marathons.")
    session.add(home)
    session.commit()


if __name__ == "__main__":
    init()
    articles()
    people()
    donations()
    text()
