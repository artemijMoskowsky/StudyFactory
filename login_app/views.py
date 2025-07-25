from .models import *
import flask

# def render_register():
#     if flask.request.method == "POST":
#         password = flask.request.form["password"]
#         email = flask.request.form["email"]
#         user = User(
#             password = password,
#             email = email
#         )
#         DATABASE.session.add(user)
#         DATABASE.session.commit()
        

#     return flask.redirect('/')

# def authorization():
#     if flask.request.method == "POST":
#         password = flask.request.form["password"]
#         email = flask.request.form["email"]
#         list_user = User.query.all()
#         for user in list_user:
#             if user.password == password and user.email == email:
#                 flask_login.login_user(user)

#     return flask.redirect('/')

def create_people():
    user1 = User(
                name = "Alex1.0",
                last_name = "White1.0",
                password = "Alex1",
                email = "email1@gmail.com"
            )
    user2 = User(
                name = "Alex2.0",
                last_name = "White2.0",
                password = "Alex2",
                email = "email2@gmail.com"
            )
    user3 = User(
                name = "Alex3.0",
                last_name = "White3.0",
                password = "Alex3",
                email = "email3@gmail.com"
            )
    
    DATABASE.session.add(user1)
    DATABASE.session.add(user2)
    DATABASE.session.add(user3)
    DATABASE.session.commit()

    return flask.redirect('/')

def clean_db():
    DATABASE.session.query(User).delete()

    return flask.redirect('/')
