from flask import render_template, request
from flask_login import current_user
from course_app.models import *

def render_home():
    if current_user.is_authenticated:
        pass
    return render_template("index.html")