from flask import render_template, request, redirect
from login_app.models import User
from .models import *

def create_course():
    course1 = Course(
        name = "Course1",
        description = "Test course",
        color = "125 54 2"
    )


    DATABASE.session.add(course1)

    course1.members.extend(User.query.all())
    course1.owners.append(User.query.first())

    DATABASE.session.commit()

    return redirect('/')