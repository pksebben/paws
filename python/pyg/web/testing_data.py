import datetime as dt
from pyg.web import models, db

# People

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
db.web.session.add(tom)

# Teams

nurples = models.Team(
    date_joined=dt.datetime.now()
)
nurples.auth = models.TeamAuth(
    name="nurples",
    password="purples"
)
nurples.profile = models.TeamAuth(
    missionstatement="we are here to make all the nurples more purrples",
    location="Chickcago",
    website="lemonparty.org",
    facebook_link="https://www.facebook.com/threateningtoliet/",
    twitter_link="twitter.com/thedonald",
    twitch_link="twitch.com"
)
db.web.session.add(nurples)

# Donations
