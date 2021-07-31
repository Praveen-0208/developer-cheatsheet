from flask import request
from application.app import app

# Import your models here
from application.services.user_service import UserService
from application.services.group_service import GroupService
from application.services.tag_service import TagService

@app.route("/")
def home():
    return {"Status": "Success"}, 200

# *********User************

@app.route("/user", methods=["POST"])
def create():
    return UserService().create_user(request.get_json())

@app.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    return UserService().get_user_by_id(id)

# **********Groups***********

@app.route("/groups", methods=["POST"])
def create_group():
    return GroupService().create_group(request.get_json())

@app.route("/groups", methods=["GET"])
def get_all_groups():
    return GroupService().get_all_groups()

@app.route("/groups/<id>", methods=["PUT"])
def update_group(id):
    return GroupService().update_group(id, request.get_json())


@app.route("/groups/<id>", methods=["DELETE"])
def delete_group(id):
    return GroupService().delete_group(id)

# ************** Tags****************
@app.route("/tags", methods=["POST"])
def create_tag():
    return TagService().create_tag(request.get_json())

@app.route("/tags", methods=["GET"])
def get_all_tags():
    return TagService().get_all_tags()

@app.route("/tags/<id>", methods=["PUT"])
def update_tag(id):
    return TagService().update_tag(id, request.get_json())


@app.route("/tags/<id>", methods=["DELETE"])
def delete_tag(id):
    return TagService().delete_tag(id)

# Write your API endpoints here
