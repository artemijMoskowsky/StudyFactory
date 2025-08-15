from login_app.app import login_app
from login_app.views import render_login, render_reg

from course_app.app import course_app
from course_app.views import render_course_creation, render_course_page, render_task_page, render_task_creation, render_delete_task, render_course_connect, render_sort

from core_app.app import core_app
from core_app.views import render_home

login_app.add_url_rule("/login", view_func=render_login, methods = ["POST", "GET"])
login_app.add_url_rule("/registration", view_func=render_reg, methods = ["POST", "GET"])

course_app.add_url_rule("/course_creation", view_func=render_course_creation, methods=["POST", "GET"])
course_app.add_url_rule("/task_creation/<int:ID>", view_func=render_task_creation, methods=["POST", "GET"])

course_app.add_url_rule("/course_page", view_func=render_course_page, methods=["POST", "GET"])
course_app.add_url_rule("/task_page", view_func=render_task_page, methods=["POST", "GET"])
course_app.add_url_rule("/course_connect/<int:ID>", view_func=render_course_connect, methods=["POST", "GET"])
course_app.add_url_rule("/s", view_func=render_sort, methods=["POST", "GET"])

core_app.add_url_rule("/", view_func=render_home, methods=["POST", "GET"])

core_app.add_url_rule("/d", view_func=render_delete_task, methods=["POST", "GET"])