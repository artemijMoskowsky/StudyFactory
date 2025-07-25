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
        yield "name", self.name
        yield "description", self.description
        yield "color", self.color
# class Task(DATABASE.Model):
#     id = DATABASE.Column(DATABASE.Integer, primary_key = True, autoincrement = True)

#     course_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("course.id"))

#     course = DATABASE.relationship("Course")