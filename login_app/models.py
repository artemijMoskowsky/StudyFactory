import flask_login
from project.db import *

class User(DATABASE.Model, flask_login.UserMixin):
    name = DATABASE.Column(DATABASE.String)
    last_name = DATABASE.Column(DATABASE.String)
    password = DATABASE.Column(DATABASE.String)
    email = DATABASE.Column(DATABASE.String)
