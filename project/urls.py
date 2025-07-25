from login_app.app import login_app
from login_app.views import render_login, render_reg
from core_app.app import core_app
from core_app.views import render_home

login_app.add_url_rule("/login", view_func=render_login, methods = ["POST", "GET"])
login_app.add_url_rule("/registration", view_func=render_reg, methods = ["POST", "GET"])
core_app.add_url_rule("/", view_func=render_home, methods=["POST", "GET"])