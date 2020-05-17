import sqlite3
from sqlite3 import Error

def sqlConn():
    try:
        con = sqlite3.connect('sql/duo.db')
        print ("Connection is established")
        return con
    except Error:
        print(Error)
        
def sqlTable(con):
    curObj = con.cursor()
    curObj.execute("CREATE TABLE translation (id integer PRIMARY KEY, target text, english text)")
    curObj.execute("CREATE TABLE learned (id integer PRIMARY KEY, target text, value integer)")
    con.commit()

try:
    con = sqlConn()
    sqlTable(con)
finally:
    con.close()