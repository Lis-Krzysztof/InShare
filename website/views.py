from flask import Blueprint, render_template
from .models import readData, readTable

views = Blueprint('views', __name__)


@views.route('/')
def home():
    all_data = readTable('SELECT * FROM ActiveOffers')
    return render_template("home.html", data = all_data)

@views.route('/search')
def search():
    all_data = readTable('SELECT * FROM ActiveOffers')
    return render_template("search.html", session=True, data = all_data)

@views.route('/choose_inpost')
def choose_inpost():
    all_data = readTable('SELECT * FROM Paczkomaty order by kod')
    return render_template("choose_inpost.html", session=True, data = all_data)


@views.route('/login')
def login():
    return render_template("login.html")