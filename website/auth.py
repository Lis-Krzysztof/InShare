from website import views
from flask import Blueprint, render_template, request, flash, redirect, session
from flask.helpers import url_for
from .models import readData, readTable, raportOffer, updatePaczkomatID

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        
        if readData('SELECT password FROM Users Where email =' +"'"+email+"'") == False:
            flash('Wrong email or password, please try again.',category='error')
            session['loggedin'] = False


        elif  readData('SELECT password FROM Users Where email =' +"'"+email+"'")[0]  == password:
            flash('Logged succesfully!', category='success')
            user = readData('SELECT * FROM Users Where email =' +"'"+email+"'")
            session['loggedin'] = True
            session['id'] = user[0]
            session['username'] = user[2]


            return redirect(url_for('views.search'))
            
        else:
            flash('Wrong email or password, please try again.',category='error')
            session['loggedin'] = False



    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
   
    return redirect(url_for('views.login'))

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
            return redirect(url_for('vievs.choose_inpost'))
        print(request.form)
        
    
    return render_template('sign_up.html')
    


@auth.route('/choose_inpost', methods = ['GET', 'POST'])
def choose_inpost():
    all_data = readTable('SELECT * FROM Paczkomaty order by kod')
    paczkomatId = request.form.get('paczkomatId')


    if request.method == 'POST':
        if paczkomatId == 'Select Paczkomat Code':
            flash('You need to set paczkomat in order to move along!', category='error')
            return render_template('choose_inpost.html', session=True, data = all_data)
        else:
            updatePaczkomatID(session['id'],paczkomatId)
            flash('Paczkomat set.', category='success')
            return redirect(url_for('views.search'))
            
    return render_template('choose_inpost.html', session=True, data = all_data)
    

@auth.route('/search', methods = ['GET', 'POST'])
def search():
    all_data = readTable('SELECT * FROM ActiveOffers')
    if request.method == 'POST' :
        
        reportDescription = request.form.get('reportDescription')
        reportType = request.form.get('reportType')
        rentForDays = request.form.get('rentForDays')
        rentOfferId = request.form.get('rentOfferId')
        reportOfferId = request.form.get('reportOfferId')
        paymentMethod = request.form.get('paymentMethod')
        print(rentForDays,rentOfferId,session['id'], paymentMethod,reportOfferId,reportType,reportDescription)

        if reportDescription and reportType and reportOfferId:
            if reportType == 'Offer expired':
                reportTypeId = 7
            elif reportType == 'Offensive content':
                reportTypeId = 4
            elif reportType == 'Offer inconsistent with the regulations':
                reportTypeId = 8
            raportOffer(reportDescription,reportTypeId,reportOfferId)
            flash(f'Raported offer: {reportType}',category='success')
            return render_template('search.html', data = all_data,session=True) 
        elif str(rentForDays).isdigit():
            if rentForDays == 1:
                flash("Rented offer for a day",category='success')
                return render_template('search.html', data = all_data,session=True)
            else:
                flash(f'Rented offer for {rentForDays} days', category='success')
                return render_template('search.html', data = all_data,session=True)
        elif str(rentForDays).isdigit() == False:
            flash('Please pass number of days you would like to rent a product!', category='error')
            return render_template('search.html', data = all_data,session=True)
        

    if session['loggedin'] == True:
        return render_template('search.html', session=True)
    else:
        return redirect(url_for('views.login'))

    


@auth.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        print(request.form)

    if session['loggedin'] == True:
        return render_template('create.html', session=True)
    else:
        return redirect(url_for('views.login'))

@auth.route('/my_offers', methods = ['GET', 'POST'])
def my_offers():
    if request.method == 'POST':
        deleteOffer = request.form.get("deleteOffer")

        if deleteOffer == 'Delete':
            flash('You succesfuly deleted your offer, reload the site to see the changes.')
        print(request.form)

    if session['loggedin'] == True:
        return render_template('my_offers.html', session=True)
    else:
        return redirect(url_for('views.login'))


