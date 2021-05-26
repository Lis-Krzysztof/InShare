from website import views
from flask import Blueprint, render_template, request, flash, redirect, session
from flask.helpers import url_for
from .models import readData, readTable, raportOffer, updatePaczkomatID,orderOffer,deleteOffer,createOffer, updateOffer, addUser
from collections.abc import Iterable

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
        surname = request.form.get('surname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        username = request.form.get('username')

        if len(email) < 3 or '@' not in email:
            flash('Invalid email', category='error')
        elif password1 != password2:
            flash('Your passwords dont match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            addUser(email, username, firstName, surname, password1)
            user = readData('SELECT * FROM Users Where email =' +"'"+email+"'")
            session['loggedin'] = True
            session['id'] = user[0]
            flash('Account created!', category='success')
            return redirect(url_for('views.choose_inpost'))
        
        
    
    return render_template('sign_up.html')
    


@auth.route('/choose_inpost', methods = ['GET', 'POST'])
def choose_inpost():
    all_data = readTable('SELECT * FROM Paczkomaty order by kod')
    paczkomatId = request.form.get('paczkomatId')


    if request.method == 'POST':
        if paczkomatId == 'Select Paczkomat Code':
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

        if reportDescription and reportType and reportOfferId:
            reportTypeId = 8
            if reportType == 'Offer expired':
                reportTypeId = 7
            elif reportType == 'Offensive content':
                reportTypeId = 4
            elif reportType == 'Offer inconsistent with the regulations':
                reportTypeId = 8
            raportOffer(reportDescription,reportTypeId,reportOfferId)
            flash(f'Raported offer: {reportType}',category='success')
            return render_template('search.html', data = all_data,session=True) 
        
        elif int(rentForDays) < 1 or int(rentForDays) > 365:
            flash('You can only rent a product between 1 and 365 days', category='error')
            return render_template('search.html', data = all_data,session=True)

        elif str(rentForDays).isdigit():
            orderOffer(session['id'],rentForDays,paymentMethod,rentOfferId)
            if rentForDays == '1':
                flash("Rented offer for a day",category='success')
            else:
                flash(f'Rented offer for {rentForDays} days', category='success')
            all_data = readTable('SELECT * FROM ActiveOffers')            
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


        offerName = request.form.get('offerName')
        offerDescription = request.form.get('offerDescription')
        offerTypeSearch = request.form.get('offerTypeSearch')
        offerValue = request.form.get('offerValue')
        offerPrice = request.form.get('offerPrice')
        offerStatus = request.form.get('offerStatus')


        if offerName == '':
            flash('Please insert offer name', category='error')
        elif offerDescription == '':
            flash('Please insert offer description', category='error')
        elif offerValue == '':
            flash('Please insert offer value', category='error')
        elif offerPrice == '':
            flash('Please insert offer price per day', category='error')
        elif str(offerValue).isdigit() == False:
            flash('Please insert correct offer value', category='error')
        elif str(offerPrice).isdigit() == False:
            flash('Please insert correct offer price per day', category='error')
        else:
            createOffer( offerName, offerDescription, session['id'], offerTypeSearch, offerValue, offerPrice, offerStatus)
            flash('Succesfully created offer!', category='succes')
            return redirect(url_for('views.my_offers'))
        

    if session['loggedin'] == True:
        return render_template('create.html', session=True)
    else:
        return redirect(url_for('views.login'))

@auth.route('/my_offers', methods = ['GET', 'POST'])
def my_offers():
    
    all_data = readTable('SELECT * FROM MyOffers WHERE userId = '+ str(session['id']))  


    if request.method == 'POST':
        deleteOfferString = request.form.get("deleteOffer")
        deleteOfferId = request.form.get('deleteOfferId')
        offerName = request.form.get('offerName')
        offerDescription = request.form.get('offerDescription')
        offerTypeId = request.form.get('offerTypeId')
        offerValue = request.form.get('offerValue')
        offerPrice = request.form.get('offerPrice')
        offerStatus = request.form.get('offerStatus')
        editOfferId = request.form.get('editOfferId')
        
        if deleteOfferString:
            if deleteOfferString.lower() == 'delete':
                deleteOffer(deleteOfferId)
                flash('You succesfuly deleted your offer',category='success')
                all_data = readTable('SELECT * FROM MyOffers WHERE userId = '+ str(session['id']) )
                return render_template('my_offers.html', session=True, data = all_data)

            else:
                flash('You have to pass word correctly in order to delete offer', category='error')


        if offerName:
            flash('Offer updated', category='success')
            updateOffer(offerName, offerDescription, offerTypeId, offerValue, offerPrice, offerStatus, editOfferId)
            all_data = readTable('SELECT * FROM MyOffers WHERE userId = '+ str(session['id']) )
            return render_template('my_offers.html', session=True, data = all_data)

    if session['loggedin'] == True:
        return render_template('my_offers.html', session=True, data = all_data)
    else:
        return redirect(url_for('views.login'))


@auth.route('/orders', methods = ['GET', 'POST'])
def orders():
    all_data = readTable('SELECT * FROM MyOrders where userId = ' + str(session['id']) + ' or userId2 = ' + str(session['id']))
            
    return render_template('orders.html', session=True, data = all_data)