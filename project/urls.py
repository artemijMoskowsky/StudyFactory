from login_app.app import login_app
from login_app.views import create_people, clean_db, render_login, render_reg

from course_app.app import course_app
from course_app.views import render_course_creation, get_all_user_courses

from core_app.app import core_app
from core_app.views import render_home

login_app.add_url_rule("/cp", view_func=create_people, methods = ["POST", "GET"])
login_app.add_url_rule("/cd", view_func=clean_db, methods = ["POST", "GET"])
login_app.add_url_rule("/login", view_func=render_login, methods = ["POST", "GET"])
login_app.add_url_rule("/registration", view_func=render_reg, methods = ["POST", "GET"])


# course_app.add_url_rule("/cc", view_func=create_course, methods=["POST", "GET"])
course_app.add_url_rule("/course_creation", view_func=render_course_creation, methods=["POST", "GET"])
course_app.add_url_rule("/get_all_user_courses", view_func=get_all_user_courses, methods=["POST", "GET"])

core_app.add_url_rule("/", view_func=render_home, methods=["POST", "GET"])
