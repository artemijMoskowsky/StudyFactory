from flask import render_template, request, redirect, Response
from flask_login import current_user
from login_app.models import User
from .models import *
import os, hashlib

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

def render_task_creation(ID):
    if request.method == "POST" and current_user.is_authenticated:
        #<a href="/task_creation/{{ course.id }}"><button>Создать задание</button></a>
        task = Task(
            name = request.form.get("name"),
            due_date = request.form.get("due_date"),
            description = request.form.get("description"),
            course_id = ID
        )
        DATABASE.session.add(task)
        DATABASE.session.commit()

        PATH = os.path.abspath(__file__ + "../../static/task_material/")
        for file in request.files.getlist("files"):
            random_salt = os.urandom(16)
            hash_name = hashlib.sha256(random_salt + file.filename.encode())
            
            file_name = file.filename.split(".")
            print(hash_name)
            if len(file_name) == 2:
                file_name.insert(1, f" {hash_name.hexdigest()}.")
                file_name = ''.join(file_name)
            else:
                file_name.insert(-1, f" {hash_name.hexdigest()}.")
                file_name = ''.join(file_name)

            file.save(os.path.join(PATH, file_name))

            file_name = file_name.split(".")
            del file_name[-1]
            "".join(file_name)
            file_name = file_name[0]

            file = File(
                file = file_name,
                task_id = task.id
            )
            DATABASE.session.add(file)
            DATABASE.session.commit()

        return redirect("/")
    
    return render_template("task_creation.html")