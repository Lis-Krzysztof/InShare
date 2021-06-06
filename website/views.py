from flask import Blueprint, render_template,redirect, url_for
from .models import readData, readTable
from flask.globals import session

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

@views.route('/my_offers')
def my_offers():
    all_data = readTable('SELECT * FROM MyOffers WHERE userId = '+ str(session['id']) )
    if all_data:
        return render_template('my_offers.html', session=True, data = all_data)
    else:
        return redirect(url_for('views.create'))

@views.route('/create')
def create():
    return render_template('create.html', session=True)