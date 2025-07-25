from flask import render_template, request

def render_home():
    return render_template("index.html")