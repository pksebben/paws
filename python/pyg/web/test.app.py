import os
import unittest
import tempfile
import random
import string
import datetime as dt

import flask
from flask import session
from sqlalchemy import Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlite3 import IntegrityError


import pyg.web.app as app
from pyg.web import auth
from pyg.web import db
from pyg.web import models
from pyg.web.views import signup, news

"""I don't like using this.  It's too workaroundy"""


def randstring(length):
    return ''.join([random.choice(string.ascii_letters)
                    for n in range(length)])


def setUpModule():
    app.init()
    models.Base.metadata.create_all(db.web.engine)


def tearDownModule():
    print("tearing down")
    models.Base.metadata.drop_all(db.web.engine)


class HomepageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tester = app.app.test_client()


class StartTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tester = app.app.test_client()
        signup.sign_new_user("othertom@gmail.com", "pass", "tom")
        signup.sign_new_user("tom@gmail.com", "pass", "tom")
        newstestcase = models.NewsArticle(
            headline="extry extry",
            author="dr seuss",
            datetime=dt.datetime.now(),
            body="there once was a man from nantucket... you know the rest",
            slug="like a snail but naked"
        )
        db.web.session.add(newstestcase)
        db.web.session.commit()
        newnewstestcase = models.NewsArticle(
            headline="read all about it",
            author="dr demento",
            datetime=dt.datetime.max,
            body="there once was a man from peru... you know the rest",
            slug="it be a living booger"
        )
        db.web.session.add(newnewstestcase)
        db.web.session.commit()

    def setUp(self):
        self.templates = []
        flask.template_rendered.connect(self._record_template, app.app)

    def tearDown(self):
        flask.template_rendered.disconnect(self._record_template, app.app)
        

    def _record_template(self, sender, template, context, **extra):
        self.templates.append(template)
        self.context = context

    # BEGIN TESTS

    # NEWS PAGE

    def test_retrieve_new_news(self):
        """test that we get the newest news article"""
        res = news.retrievenews(news.latestnews())
        self.assertEqual(res.headline, "read all about it")

    def test_news_page_available(self):
        """test that the news page renders and serves a story"""
        res = self.tester.get('/news', content_type="html/text")
        self.assertIn(b"demento", res.data)

    # END NEWS PAGE

    def test_app_available(self):
        """check if the app makes itself available"""
        res = self.tester.get('/', content_type="html/text")
        self.assertEqual(res.status_code, 200)

    def test_index_content(self):
        """checks if the homepage is served up correctly"""
        res = self.tester.get('/', content_type="html/text")
        self.assertIn(b'Paws Your Game', res.data)
        self.assertEqual(self.templates[0].name, "content_home.html")
        print(self.context)

    def test_db_available(self):
        """tests if the database exists"""
        self.assertTrue(os.path.exists("foo.db"))

    def signup_new_user(self, email="tom@gmail.com",
                        password="pass", name="tom"):
        id = signup.sign_new_user(email, password, name)
        return id

    def test_signup_new_user_success(self):
        """does signup.sign_new_user properly add users?"""
        thisemail = "tbob@gmail.com"
        id = self.signup_new_user(email=thisemail)
        res = db.web.session.query(
            models.UserAuth).get(id)
        self.assertEqual(thisemail, res.email)

    def test_signup_new_user_exists(self):
        pass

    def test_signup_new_user_bad_email(self):
        """test that emails are validated appropriately"""
        pass

    def test_signup_new_user_bad_password(self):
        """test that passwords are validated for length, characters, etc."""
        pass

    def test_signup_new_user_noname(self):
        """test that signup fails if no name is provided.  Do we want this?"""
        pass

    # SEARCH PAGE

    def test_wherestom(self):
        res = db.web.session.query(models.UserAuth).filter_by(name="tom")
        self.assertEqual("tom", res.first().name)

    def test_manytoms(self):
        res = db.web.session.query(models.UserAuth).filter_by(name="tom").all()
        self.assertEqual("tom", res[0].name)

    def test_search_name_tom(self):
        # might be doing the post request wrong
        res = self.tester.post('/search', data=dict(
            name="tom"
        ))
        self.assertIn(b"tom", res.data)

    def test_search_name_absent_beelzebub(self):
        # might be doing the post request wrong
        res = self.tester.post('/search', data=dict(
            name="beelzebub"
        ))
        self.assertNotIn(b"beelzebub", res.data)

    # END SEARCH

    def test_user_login(self):
        """test that auth.user works to log a user in"""
        with app.app.test_request_context():
            auth.user("tom@gmail.com", "pass")
            self.assertIn("userid", session)

    def test_userprofile_update_notloggedin(self):
        pass

    def test_userprofile_update_bad_input(self):
        pass


if __name__ == '__main__':
    unittest.main()
