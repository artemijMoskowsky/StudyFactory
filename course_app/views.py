from flask import render_template, request, redirect, Response
from flask_login import current_user
from sqlalchemy import event
from login_app.models import User
from .models import *
import os, hashlib

#Автоудаление файлов при удалении его из Б.Д.

def delete_file_from_static(mapper, connection, target):
    BASE_DIR = os.path.abspath(__file__ + "../../")
    MATERIALS_PATH = os.path.abspath(os.path.join(BASE_DIR, "static", "task_material"))
    
    file_path = os.path.join(MATERIALS_PATH, target.file)
    if os.path.exists(file_path):
        os.remove(file_path)
        
event.listen(File, 'after_delete', delete_file_from_static)

#-----------------------------------------------------------

def render_course_creation():
    if request.method == "POST" and current_user.is_authenticated:
        course = Course(
            name = request.form.get("name"),
            description = request.form.get("description"),
            color = request.form.get("color")
        )

        DATABASE.session.add(course)

        course.owners.append(current_user)

        DATABASE.session.commit()

        hash_course = HashCourse(
            hash = course.id,
            course_id = course.id
        )
        DATABASE.session.add(hash_course)
        DATABASE.session.commit()

        return redirect("/")
    
    return render_template("course_creation.html")

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
            if file.filename != "":
                random_salt = os.urandom(16)
                hash_name = hashlib.sha256(random_salt + file.filename.encode())
                
                file_name = file.filename.split(".")

                if len(file_name) == 2:
                    file_name.insert(1, f" {hash_name.hexdigest()}.")
                    file_name = ''.join(file_name)
                else:
                    file_name.insert(-1, f" {hash_name.hexdigest()}.")
                    file_name = ''.join(file_name)

                file.save(os.path.join(PATH, file_name))

                file = File(
                    file = file_name,
                    task_id = task.id
                )
                DATABASE.session.add(file)
                DATABASE.session.commit()

        return redirect("/")
    
    return render_template("task_creation.html")


def render_task_page():
    return render_template("task_page.html")


def render_course_page():
    return render_template("course_page.html")


def render_delete_task():
    task = Task.query.get(1)
    files = File.query.filter_by(task_id=task.id).all()

    BASE_DIR = os.path.abspath(__file__ + "../../")
    MATERIALS_PATH = os.path.abspath(os.path.join(BASE_DIR, "static", "task_material"))

    for file in files:
        file_path = os.path.join(MATERIALS_PATH, file.file)
        print(file_path)
        os.remove(file_path)

    DATABASE.session.delete(task)
    DATABASE.session.commit()

    return redirect("/")


def render_course_connect(ID):
    course = Course.query.get(ID)
    course.members.append(current_user)
    DATABASE.session.commit()

    return redirect("/")


def render_finish_task(ID):
    if request.method == "POST" and current_user.is_authenticated:
        #<a href="/task_creation/{{ task.id }}"><button>Сдать задание</button></a>
        f_task = Submitted_Assignments(
            user_id = current_user.id,
            task_id = ID
        )
        DATABASE.session.add(f_task)
        DATABASE.session.commit()

        PATH = os.path.abspath(__file__ + "../../static/students_material/")
        for file in request.files.getlist("files"):
            if file.filename != "":
                random_salt = os.urandom(16)
                hash_name = hashlib.sha256(random_salt + file.filename.encode())
                
                file_name = file.filename.split(".")

                if len(file_name) == 2:
                    file_name.insert(1, f" {hash_name.hexdigest()}.")
                    file_name = ''.join(file_name)
                else:
                    file_name.insert(-1, f" {hash_name.hexdigest()}.")
                    file_name = ''.join(file_name)

                file.save(os.path.join(PATH, file_name))

                s_file = Submitted_Assignments_File(
                    file = file_name,
                    submission_id = f_task.id
                )
                DATABASE.session.add(s_file)
                DATABASE.session.commit()

        return redirect("/")
    
    return render_template("finish_task.html")


#Сортировка-срока-сдачи-заданий-------------------------------------------------------------------
def swap(list: list, i: int, j: int):
    list[i], list[j] = list[j], list[i]
    return list


def parse_date(date_str: str):
    date_str = date_str.split("-")

    time = date_str[2].split("T")
    date_str[2] = time[0]
    date_str.append(time[1])

    time_d = date_str[3].split(":")
    date_str[3] = time_d[0]
    date_str.append(time_d[1])
    
    return list(map(int, date_str))


def comparison_date(date_f: list, date_s: list):
    for i in range(5):
        if date_f[i] > date_s[i]:
            return True
        
        elif date_f[i] < date_s[i]:
            return False
        
    return False #одинаковое


def sort_date(list: list):
    sorted_list_of_date = list
    for j in range(len(list)):
        for date in list:
            index = list.index(date)
            date = parse_date(date)

            if index != len(list) - 1:
                date_s = list[index + 1]
                date_s = parse_date(date_s)
                
                answer = comparison_date(date, date_s)
                if answer:
                    sorted_list_of_date = swap(sorted_list_of_date, index, index + 1)

    return sorted_list_of_date

def render_sort():
    courses = current_user.courses
    list_tasks = []
    for i in range(len(courses)):
        list_tasks.append(courses[i].tasks)

    list_of_date = []
    for sublist in list_tasks:
        for task in sublist:
            list_of_date.append(task.due_date)

    sorted_list = sort_date(list_of_date)

    return render_template("course_page.html")