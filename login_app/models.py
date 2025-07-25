import flask_login
from project.db import *

class User(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String)
    surname = DATABASE.Column(DATABASE.String)
    password = DATABASE.Column(DATABASE.String)
    email = DATABASE.Column(DATABASE.String)
