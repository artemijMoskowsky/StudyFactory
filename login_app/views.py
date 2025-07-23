from .models import *
import flask

def render_register():
    if flask.request.method == "POST":
        name = flask.request.form["username"]
        email = flask.request.form["email"]
        user = User(
            name = name,
            email = email
        )
        DATABASE.session.add(user)
        DATABASE.session.commit()
        

    return flask.redirect('/')

def authorization():
    if flask.request.method == "POST":
        name = flask.request.form["name"]
        email = flask.request.form["email"]
        list_user = User.query.all()
        for user in list_user:
            if user.name == name and user.email == email:
                flask_login.login_user(user)

    return flask.redirect('/')

def create_people():
    user1 = User(
                name = "Alex1",
                email = "email1@gmail.com"
            )
    user2 = User(
                name = "Alex2",
                email = "email2@gmail.com"
            )
    user3 = User(
                name = "Alex3",
                email = "email3@gmail.com"
            )
    
    DATABASE.session.add(user1)
    DATABASE.session.add(user2)
    DATABASE.session.add(user3)
    DATABASE.session.commit()

    return flask.redirect('/')

def clean_db():
    DATABASE.session.session.query(User).delete()

    return flask.redirect('/')