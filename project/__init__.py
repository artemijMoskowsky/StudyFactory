from .urls import *
from .settings import *
from .db import *
from .loadenv import *
from .login_manager import *

from login_app.app import *

project.register_blueprint(blueprint = login_app)