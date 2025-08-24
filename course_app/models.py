from project.db import DATABASE
from datetime import datetime

owners_and_courses_table = DATABASE.Table("owners_and_courses", DATABASE.metadata, 
                                          DATABASE.Column("user_id", DATABASE.ForeignKey("user.id")),
                                          DATABASE.Column("course_id", DATABASE.ForeignKey("course.id")))

members_and_courses_table = DATABASE.Table("members_and_courses", DATABASE.metadata, 
                                          DATABASE.Column("user_id", DATABASE.ForeignKey("user.id")),
                                          DATABASE.Column("course_id", DATABASE.ForeignKey("course.id")))

class Course(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)

    name = DATABASE.Column(DATABASE.String(50))
    
    description = DATABASE.Column(DATABASE.Text)
    
    color = DATABASE.Column(DATABASE.String(7))

    owners = DATABASE.relationship("User", secondary = owners_and_courses_table, backref = "owned_courses")

    members = DATABASE.relationship("User", secondary = members_and_courses_table, backref = "courses")

    tasks = DATABASE.relationship("Task", backref="course", cascade="all, delete-orphan")
    messages = DATABASE.relationship("Message_Course", backref="course", cascade="all, delete-orphan")

    hash = DATABASE.relationship("HashCourse", backref="course", cascade="all, delete-orphan")

    def __iter__(self):
        yield "id", self.id
        yield "name", self.name
        yield "description", self.description
        yield "owner", f"{self.owners[0].name} {self.owners[0].surname}" if len(self.owners) > 0 else "Not found"
        yield "color", self.color


class HashCourse(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)

    hash = DATABASE.Column(DATABASE.String)

    course_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("course.id"), unique=True)


class Task(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True, autoincrement = True)

    name = DATABASE.Column(DATABASE.String(100))
    description = DATABASE.Column(DATABASE.String(100))
    due_date = DATABASE.Column(DATABASE.String) #Поменять при необходимости

    time_send = DATABASE.Column(DATABASE.DateTime, default=datetime.utcnow)

    course_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("course.id"))

    urls = DATABASE.relationship("Url", backref="task", cascade="all, delete-orphan")
    files = DATABASE.relationship("File", backref="task", cascade="all, delete-orphan")
    messages = DATABASE.relationship("Message_Task", backref="task", cascade="all, delete-orphan")

    def __iter__(self):
        yield "id", self.id
        yield "name", self.name
        yield "description", self.description
        yield "time_send", self.time_send
        yield "due_date", self.due_date

class Url(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True, autoincrement = True)

    url = DATABASE.Column(DATABASE.String)

    task_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("task.id"))


class File(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True, autoincrement = True)

    file = DATABASE.Column(DATABASE.String)

    task_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("task.id"))


class Message_Course(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True, autoincrement = True)


    now = datetime.utcnow()
    time_send = DATABASE.Column(DATABASE.DateTime, default=now.isoformat())
    message_text = DATABASE.Column(DATABASE.String)

    course_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("course.id"))

    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("user.id"))


class Message_Task(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True, autoincrement = True)

    message_text = DATABASE.Column(DATABASE.String)
    now = datetime.utcnow()
    time_send = DATABASE.Column(DATABASE.DateTime, default=now.isoformat())

    task_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("task.id"))

    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("user.id"))


#Модели-для-сданных-заданий-от-ученика------------------------------------------------------------
class Submitted_Assignments(DATABASE.Model):
    __tablename__ = 'submitted_assignments'
    id = DATABASE.Column(DATABASE.Integer, primary_key=True, autoincrement = True)

    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("user.id"))
    task_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("task.id"))

    user = DATABASE.relationship("User", backref="submissions_user")
    
    files = DATABASE.relationship("Submitted_Assignments_File", backref="submitted_assignments")



class Submitted_Assignments_File(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)

    file = DATABASE.Column(DATABASE.String)

    submission_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("submitted_assignments.id"))