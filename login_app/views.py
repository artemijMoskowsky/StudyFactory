from flask import render_template, request

def render_login():
    return render_template("login.html")

def render_reg():
    return render_template("reg.html")