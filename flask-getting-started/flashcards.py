from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"


@app.route("/date")
def date():
    return f"This page was served at {str(datetime.now())}"


# Task: add a page that shows number of times a page is visited!
number_of_times = 0

@app.route("/page_visit_count")
def page_visit_count():
    global number_of_times
    number_of_times += 1
    return f"This page is visited {number_of_times} times"
