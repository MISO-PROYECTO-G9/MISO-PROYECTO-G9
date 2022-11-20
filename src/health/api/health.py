from flask import Blueprint
from injector import inject

health = Blueprint('health', __name__)


@health.route('/ping/', methods=['GET'])
@inject
def check():
    return "pong", 200


@health.route('/fail/', methods=['GET'])
@inject
def fail():
    return "pong", 404