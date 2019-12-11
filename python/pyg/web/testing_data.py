import random
import datetime as dt

from pyg.web import models, db


"""
This has been factored into it's own module to allow testing of the site in test.app.py as well as by running the app.
"""


def makesomeboyees():
    try:
        tom = models.Person(
            created=dt.datetime.now()
        )
        tom.auth = models.UserAuth(
            name="tom",
            password="pass",
            email="tom@gmail.com"
        )
        tom.profile = models.UserProfile(
            about="my name is tom.  I am not good with about sections",
            birthday=dt.datetime.now(),
            location="The town of hogsface, Land of foon"
        )
        othertom = models.Person(
            created=dt.datetime.now()
        )
        othertom.auth = models.UserAuth(
            name="tom",
            password="pass",
            email="othertom@gmail.com"
        )
        othertom.profile = models.UserProfile(
            about="my name is other tom.  I am not good with about sections",
            birthday=dt.datetime.now(),
            location="The town of hogsface, Land of foon"
        )
        bob = models.Person(
            created=dt.datetime.now()
        )
        bob.auth = models.UserAuth(
            name="bob",
            password="pass",
            email="bob@gmail.com"
        )
        bob.profile = models.UserProfile(
            about="my name is bob.  I am not good with about sections",
            birthday=dt.datetime.now(),
            location="The town of pigsface, Land of foon"
        )
        bill = models.Person(
            created=dt.datetime.now()
        )
        bill.auth = models.UserAuth(
            name="bill",
            password="pass",
            email="bill@gmail.com"
        )
        bill.profile = models.UserProfile(
            about="my name is bill.  I am not good with about sections",
            birthday=dt.datetime.now(),
            location="The town of hogsface, Land of foon"
        )

        nurples = models.Team(
            date_joined=dt.datetime.now()
        )
        nurples.auth = models.TeamAuth(
            name="nurples",
            password="purples"
        )
        nurples.profile = models.TeamProfile(
            missionstatement="we are here to make all the nurples more purrples",
            location="Chickcago",
            website="lemonparty.org",
            facebook_link="https://www.facebook.com/threateningtoliet/",
            twitter_link="twitter.com/thedonald",
            twitch_link="twitch.com"
        )
        db.web.session.add(nurples)

        # Donations
        playerslist = [bill, tom, bob]
        donationslist = [models.Donation() for i in range(50)]
        for i in donationslist:
            random.choice(playerslist).donations.append(i)
            i.amount = random.randint(5, 1500)
            i.created = dt.datetime.now()
            i.donor_name = "mr moneybags"
            db.web.session.add(i)

        db.web.session.add(othertom)
        db.web.session.add(bill)
        db.web.session.add(tom)
        db.web.session.add(bob)
        db.web.session.commit()
    except Exception as err:
        print(err)
