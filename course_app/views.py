from flask import render_template, request, redirect, Response
from flask_login import current_user
from login_app.models import User
from .models import *

def render_course_creation():
    if request.method == "POST" and current_user.is_authenticated:
        print(current_user)
        course = Course(
            name = request.form.get("name"),
            description = request.form.get("description"),
            color = request.form.get("color")
        )

        DATABASE.session.add(course)

        course.owners.append(current_user)

        DATABASE.session.commit()

        return redirect("/")
    
    return render_template("course_page.html") ###############################################################

def get_info_about_course(id: str):
    course = Course.query.filter(id = id)
    if course:
        return Response(course.__dict__, 200)
    return Response("Error", 404)

def get_all_user_courses():
    if current_user.is_authenticated:
        courses = Course.query.filter(Course.owners.any(User.id == current_user.id)).all()
        data = [dict(course) for course in courses]
        print(data)
        return data
    return "None"