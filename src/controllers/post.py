"""Docstring checker from the basic checker."""

from mocks.data import posts
from database.connect import database
from models.model import Post

result = database()


def get_posts():
    result.execute('select * from posts')
    return result.fetchall()


def create(post: Post):
    print(type(post.description))
    description = str(post.description)
    result.execute(
        "INSERT INTO test (description) VALUES (%s)",  (description))
    result.fetchone()


def find_post(id):
    for resp in posts:
        if resp['id'] == id:
            return resp


def find_index(id):
    for index, item in enumerate(posts):
        if item['id'] == id:
            return index
