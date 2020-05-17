import sqlite3
from sqlite3 import Error

def sqlConn():
    try:
        con = sqlite3.connect('sql/duo.db')
        print ("Connection is established")
        return con
    except Error:
        print (Error)
        
def createTable(con):
    curObj = con.cursor()
    try:
        curObj.execute("CREATE TABLE translation (target text PRIMARY KEY, english text)")
        con.commit()
    except Error:
        print (Error)

def hashToTable(con, entries):
    curObj = con.cursor()
    try:
        for entry in entries:
            curObj.execute("INSERT INTO translation(target, english) VALUES(?, ?)", entry)
            con.commit()
    except Error:
        pass

def tableToHash(con):
    wordHash = {}
    curObj = con.cursor()
    curObj.execute('SELECT target, english FROM translation')
    rows = curObj.fetchall()
    for row in rows:
        wordHash[row[0]] = row[1]
    return wordHash

def numOfEntries(con):
    curObj = con.cursor()
    curObj.execute('SELECT target, english FROM translation')
    rows = curObj.fetchall()
    count = len(rows)
    return count
    
# TODO:
# Get data from self.pullVocab()
# Conditional statement to see if rows have been populated
# if not, then self.dataToModel() then store data into persistent storage
# if yes, then condiitonal statement and pull data from table using tableToHash method, skipping the slow google api module

try:
    con = sqlConn()
    entries = [('casa', 'house'), ('bien', 'good'), ('hermano', 'brother')]
    createTable(con)
    hashToTable(con, entries)
    count = numOfEntries(con)
    print (count)
    wordHash = tableToHash(con)
    print (wordHash)
    
finally:
    con.close()