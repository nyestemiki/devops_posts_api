from post import Post
import time
from flask import json


def get_post_by_id(posts, id):
    for post in posts:
        if post.id == id:
            return post

    return None


def get_post_from_request(request, id):
    return Post(id, request.get('title'),
                request.get('description'), request.get('userId'), time.time())


def update_post_from_request(request, post):
    title = request.get('title')
    if title:
        post.title = title

    description = request.get('description')
    if description:
        post.description = description

    userId = request.get('userId')
    if userId:
        post.userId = userId

    post.date = time.time()

def dump_posts(posts):
    return json.dumps([post.get_object() for post in posts])
