from .urls import *
from .settings import *
from .db import *
from .loadenv import *
from .login_manager import *
from core_app.app import *

from login_app.app import *

from course_app.app import *

from core_app.app import *

project.register_blueprint(blueprint = login_app)
project.register_blueprint(blueprint = course_app)
project.register_blueprint(blueprint = core_app)