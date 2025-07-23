import flask_login
from project.db import *

class User(DATABASE.Model, flask_login.UserMixin):
    password = DATABASE.Column(DATABASE.String)
    email = DATABASE.Column(DATABASE.String)
