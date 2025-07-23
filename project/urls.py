from login_app.app import login_app
from login_app.views import render_login, render_reg

login_app.add_url_rule("login/", view_func=render_login, methods = ["POST", "GET"])
login_app.add_url_rule("registration/", view_func=render_reg, methods = ["POST", "GET"])