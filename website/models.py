import pyodbc
import base64


query='SELECT * FROM dbo.ActiveOffers'




def readData(query):
    server = '.' 
    database = 'InShare' 
    username = 'user2' 
    password = "A"
    con = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+'; DATABASE='+database+'; UID='+username+';PWD='+password, autocommit=True)
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    if not data:
        cur.close()
        return False
    else:
        for row in data:
            row_to_list = [elem for elem in row]
        cur.close()
        return row_to_list
    
def readTable(query):
    server = '.' 
    database = 'InShare' 
    username = 'user2' 
    password = "A"
    con = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+'; DATABASE='+database+'; UID='+username+';PWD='+password, autocommit=True)
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    if not data:
        cur.close()
        return False
    else:
        cur.close()
        return data

def raportOffer(reportDescription,reportTypeId,reportOfferId):
    server = '.' 
    database = 'InShare' 
    username = 'user2' 
    password = "A"
    con = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+'; DATABASE='+database+'; UID='+username+';PWD='+password, autocommit=True)
    cur = con.cursor()
    query =  'EXECUTE reportOffer @reportTypeId = ' + str(reportTypeId) +', @description = ' + "'" + reportDescription + "'" + f', @offerId = {reportOfferId} '
    cur.execute(query)
    cur.close()

def updatePaczkomatID(userId,paczkomatId):
    server = '.' 
    database = 'InShare' 
    username = 'user2' 
    password = "A"
    con = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+'; DATABASE='+database+'; UID='+username+';PWD='+password, autocommit=True)
    cur = con.cursor()
    query =  f'EXECUTE updatePaczkomatID @userId = {userId}, @paczkomatId = {paczkomatId} '
    cur.execute(query)
    cur.close()


def orderOffer(borrowedTo, days, paymentMetodId, offerId):
    server = '.' 
    database = 'InShare' 
    username = 'user2' 
    password = "A"
    con = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+'; DATABASE='+database+'; UID='+username+';PWD='+password, autocommit=True)
    cur = con.cursor()
    query =  f'EXECUTE orderOffer @borrowedTo = {borrowedTo}, @days = {days} , @paymentMetodId = {paymentMetodId}, @offerId = {offerId}'
    cur.execute(query)
    cur.close()


def deleteOffer(offerId):
    server = '.' 
    database = 'InShare' 
    username = 'user2' 
    password = "A"
    con = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+'; DATABASE='+database+'; UID='+username+';PWD='+password, autocommit=True)
    cur = con.cursor()
    query =  f'EXECUTE deleteOffer @offerId = {offerId}'
    cur.execute(query)
    cur.close()

def createOffer( Name, Description, userId, offerTypeId, value, price_per_day, offerStatusId):
    server = '.' 
    database = 'InShare' 
    username = 'user2' 
    password = "A"
    con = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+'; DATABASE='+database+'; UID='+username+';PWD='+password, autocommit=True)
    cur = con.cursor()
    query =  'EXECUTE createOffer @Name = ' + "'" + str(Name) + "'" +', @Description = ' + "'" + str(Description) + "'" +',@userId = ' + str(userId) +',@offerTypeId = ' + str(offerTypeId) +',@value = ' + str(value) +',@price_per_day = ' + str(price_per_day) +',@offerStatusId = ' + str(offerStatusId) 
    cur.execute(query)
    cur.close()

def updateOffer(Name, Description, offerTypeId, value, price_per_day, offerStatusId, offerId):
    server = '.' 
    database = 'InShare' 
    username = 'user2' 
    password = "A"
    con = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+'; DATABASE='+database+'; UID='+username+';PWD='+password, autocommit=True)
    cur = con.cursor()
    query =  'EXECUTE updateOffer @Name = ' + "'" + str(Name) + "'" + ', @Description = ' + "'" + str(Description) + "'"  + ',@offerTypeId = ' + str(offerTypeId) + ',@value = ' + str(value) +',@price_per_day = ' + str(price_per_day) +',@offerStatusId = ' + str(offerStatusId) +',@offerId = ' + str(offerId) 
    cur.execute(query)
    cur.close()

def addUser(email, userName, Name, Surname, password):
    server = '.' 
    database = 'InShare' 
    username = 'user2' 
    password = "A"
    con = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+'; DATABASE='+database+'; UID='+username+';PWD='+password, autocommit=True)
    cur = con.cursor()
    query =  'EXECUTE addUser @email = ' + "'" + str(email) + "'" + ', @userName = ' + "'" + str(userName) + "'"  + ',@Name = ' + str(Name) + ',@Surname = ' + str(Surname) +',@password = ' + str(password)
    cur.execute(query)
    cur.close()