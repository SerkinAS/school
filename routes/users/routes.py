from flask import Blueprint

users = Blueprint('users', __name__, template_folder='users')


@users.route('/users/login', methods=['GET'])
def login():
    return ''
