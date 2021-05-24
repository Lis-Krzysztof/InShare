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