from flask import json


class Post:
    def __init__(self, id, title, description, userId, date) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.userId = userId
        self.date = date

    def get_object(self):
        post_object = {}
        post_object["id"] = self.id
        post_object["title"] = self.title
        post_object["description"] = self.description
        post_object["userId"] = self.userId
        post_object["date"] = self.date

        return post_object

    def dump(self):
        return json.dumps(self.get_object())
