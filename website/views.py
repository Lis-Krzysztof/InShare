from flask import Blueprint, render_template
from flask.globals import session

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/search')
def search():
    return render_template("search.html", session=True)

@views.route('/choose_inpost')
def choose_inpost():
    return render_template("choose_inpost.html", session=True)


@views.route('/login')
def login():
    return render_template("login.html")