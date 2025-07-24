from .models import *
import flask

def render_reg():
    if flask.request.method == "POST":
        name = flask.request.form["name"]
        surname = flask.request.form["surname"]
        password = flask.request.form["password"]
        confirm_password = flask.request.form["confirm-password"]
        email = flask.request.form["email"]
        if confirm_password == password:
            user = User(
                name = name,
                surname = surname,
                password = password,
                email = email
            )
            DATABASE.session.add(user)
            DATABASE.session.commit()
            return flask.redirect('/')
        
    return flask.render_template("reg.html")
        


def render_login():
    if flask.request.method == "POST":
        password = flask.request.form["password"]
        email = flask.request.form["email"]
        list_user = User.query.all()
        for user in list_user:
            if user.password == password and user.email == email:
                flask_login.login_user(user)
                return flask.redirect('/')
            
    return flask.render_template("login.html")

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
    DATABASE.session.delete()

    return flask.redirect('/')
