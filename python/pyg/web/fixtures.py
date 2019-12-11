import datetime

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


if __name__ == "__main__":
    init()
    articles()
