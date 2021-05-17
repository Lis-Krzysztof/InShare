from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)

    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 3 or '@' not in email:
            flash('Invalid email', category='error')
        elif password1 != password2:
            flash('Your passwords dont match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Account created!', category='success')
            return render_template('choose_inpost.html')
        print(request.form)
        

    return render_template('sign_up.html')


@auth.route('/choose_inpost', methods = ['GET', 'POST'])
def choose_inpost():
    if request.method == 'POST':
        print(request.form)

    return render_template('choose_inpost.html')

@auth.route('/search', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST' :
        reportDescription = request.form.get('reportDescription')
        reportType = request.form.get('reportType')
        rentForDays = request.form.get('rentForDays')

        if reportDescription:
            flash(f'Raported offer: {reportType}',category='success')
            return render_template('search.html') 
        elif str(rentForDays).isdigit():
            if rentForDays == 1:
                flash("Rented offer for a day",category='success')
                return render_template('search.html')
            else:
                flash(f'Rented offer for {rentForDays} days', category='success')
                return render_template('search.html')
        elif str(rentForDays).isdigit() == False:
            flash('Please pass number of days you would like to rent a product!', category='error')
            return render_template('search.html')
        print(request.form)

    return render_template('search.html')

@auth.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        print(request.form)

    return render_template('create.html')

@auth.route('/my_offers', methods = ['GET', 'POST'])
def my_offers():
    if request.method == 'POST':
        deleteOffer = request.form.get("deleteOffer")

        if deleteOffer == 'Delete':
            flash('You succesfuly deleted your offer, reload the site to see the changes.')
        print(request.form)

    return render_template('my_offers.html')


