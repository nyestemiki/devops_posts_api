from flask import Flask, json, request
from log import Log, log
from helpers import get_post_from_request, update_post_from_request, dump_posts, get_post_by_id
from request import Request

# id, title, description, userId, date
posts = []

api = Flask(__name__)


@api.route('/', methods=['GET'])
def get():
    log(Log(Request.GET, "/"))

    return json.dumps("All good")


@api.route('/posts', methods=['GET'])
def get_posts():
    log(Log(Request.GET, "/posts"))

    return dump_posts(posts)


@api.route('/post/<id>', methods=['GET'])
def get_post(id):
    log(Log(Request.GET, "/post/" + id))

    post = get_post_by_id(posts, id)
    if post is None:
        return json.dumps('Not found')

    return post.dump()


@api.route('/post', methods=['POST'])
def post_post():
    log(Log(Request.POST, "/post"))

    post = get_post_from_request(request.get_json(), str(len(posts) + 1))
    posts.append(post)

    return post.dump()


@api.route('/post/<id>', methods=['PUT'])
def put_post(id):
    log(Log(Request.PUT, "/post/" + id))

    post = get_post_by_id(posts, id)

    if post is None:
        return json.dumps("Not found")

    update_post_from_request(request.get_json(), post)

    return post.dump()


@api.route('/post/<id>', methods=['DELETE'])
def delete_post(id):
    log(Log(Request.DELETE, "/post/id" + id))

    post = get_post_by_id(posts, id)

    if post is None:
        return json.dumps("Not found")

    posts.remove(post)
    return json.dumps("Deleted")


if __name__ == '__main__':
    api.run(host='0.0.0.0')
