from project.db import DATABASE

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

    def __iter__(self):
        yield "id", self.id
        yield "name", self.name
        yield "description", self.description
        yield "owner", f"{self.owners[0].name} {self.owners[0].surname}" if len(self.owners) > 0 else "Not found"
        yield "color", self.color


class Task(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True, autoincrement = True)

    name = DATABASE.Column(DATABASE.String(100))
    description = DATABASE.Column(DATABASE.String(100))
    due_date = DATABASE.Column(DATABASE.String) #Поменять при необходимости

    course = DATABASE.relationship("Course", backref = "tasks")
    course_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("course.id"))


class Url(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True, autoincrement = True)

    url = DATABASE.Column(DATABASE.String)

    task = DATABASE.relationship("Task", backref = "urls")
    task_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("task.id"))


class File(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True, autoincrement = True)

    file = DATABASE.Column(DATABASE.String)

    task = DATABASE.relationship("Task", backref = "files")
    task_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("task.id"))