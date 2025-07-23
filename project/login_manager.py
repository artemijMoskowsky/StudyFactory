import flask_login
from .settings import *
from login_app.models import *

project.secret_key = 'key'

login_manager = flask_login.LoginManager(app = project)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
