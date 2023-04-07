#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

from app import app
from models import db, Author, Post


fake = Faker()

with app.app_context():

    Author.query.delete()
    Post.query.delete()

    # author1 = Author(name="John", phone_number= 1234)
    # db.session.add(author1)
    # db.session.commit()

    post1 = Post(title="Hello", content="Lots of secrets" * 70, summary="Whole lotta secrets", category="Fiction")

    # authors = []
    # for n in range(25):
    #     author = Author(name=fake.name(), phone_number='1324543333')
    #     authors.append(author)

    # db.session.add_all(authors)
    # posts = []
    # for n in range(25):
    #     post = Post(title='Secret banana', content='This is the content Secret' * 50, category= 'Fiction', summary="Summary Secret" )
    #     posts.append(post)

    # db.session.add_all(posts)

    # db.session.commit()