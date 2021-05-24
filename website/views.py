from flask import Blueprint, render_template
<<<<<<< HEAD
from .models import readData, readTable
=======
from flask.globals import session
>>>>>>> 676ac8badbf7b7f069fa29c94ee0f848a10dea7b

views = Blueprint('views', __name__)


@views.route('/')
def home():
<<<<<<< HEAD
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
=======
    return render_template("home.html")

@views.route('/search')
def search():
    return render_template("search.html", session=True)

@views.route('/choose_inpost')
def choose_inpost():
    return render_template("choose_inpost.html", session=True)
>>>>>>> 676ac8badbf7b7f069fa29c94ee0f848a10dea7b


@views.route('/login')
def login():
    return render_template("login.html")