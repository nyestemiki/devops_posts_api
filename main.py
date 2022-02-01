from flask import Flask, json, request
import logging
import time

logging.basicConfig(filename='./posts_api/logs/debug.log', level=logging.DEBUG)

# id, title, description, userId, date
posts = []

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get():
  return json.dumps("All good")

@api.route('/posts', methods=['GET'])
def get_posts():
  return json.dumps(posts)

@api.route('/post/<id>', methods=['GET'])
def get_post(id):
  return json.dumps(get_post_by_id(id))

@api.route('/post', methods=['POST'])
def post_post():
    request_data = request.get_json()

    post = {}
    post["id"] = str(len(posts) + 1)
    post["title"] = request_data.get('title')
    post["description"] = request_data.get('description')
    post["userId"] = request_data.get('userId')
    post["date"] = time.time()

    posts.append(post)

    return json.dumps(post)

@api.route('/post/<id>', methods=['PUT'])
def put_post(id):
    post = get_post_by_id(id)

    if post is None:
        return json.dumps("Not found")

    request_data = request.get_json()

    title = request_data.get('title')
    if title:
        post["title"] = title

    description = request_data.get('description')
    if description:
        post["description"] = description

    userId = request_data.get('userId')    
    if userId:
        post["userId"] = userId

    post["date"] = time.time()

    return json.dumps(post)


@api.route('/post/<id>', methods=['DELETE'])
def delete_post(id):
    post = get_post_by_id(id)

    if post is None:
        return json.dumps("Not found")

    posts.remove(post)
    return json.dumps("Deleted")

def get_post_by_id(id):
    for post in posts:
        if post["id"] == id:
            return post
    
    return None

if __name__ == '__main__':
    api.run(host='0.0.0.0')