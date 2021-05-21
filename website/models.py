import pyodbc
import base64


query='SELECT * FROM dbo.Users'




def readData(query):
    server = '.' 
    database = 'test1' 
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
    
readData(query)