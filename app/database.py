import sqlite3
from sqlite3 import Error

class Database:
    """
        Class that contains the methods that interact with the 'backend' and data of the program
        
    """
    def __init__(self):
        self.con = None
        self.cur = None
        self.sqlConn()
        self.createTable() # Make  check to see if table already exists!
    
    def sqlConn(self):
        try:
            self.con = sqlite3.connect('sql/duo.db')
            self.cur = self.con.cursor()
        except Error:
            print (Error)
        
    def createTable(self):
        try:
            self.cur.execute("CREATE TABLE translation (target text PRIMARY KEY, english text)")
            self.con.commit()
        except Error:
            print (Error)

    def hashToTable(self, hashmap):
        try:
            for key, value in hashmap.items():
                self.cur.execute("INSERT INTO translation(target, english) VALUES(?, ?)", (key, value))
                self.con.commit()
        except Error:
            print (Error)

    def tableToHash(self):
        wordHash = {}
        self.cur.execute("SELECT target, english FROM translation")
        rows = self.cur.fetchall()
        for row in rows:
            wordHash[row[0]] = row[1]
        return wordHash

    def numOfEntries(self):
        self.cur.execute("SELECT target, english FROM translation")
        rows = self.cur.fetchall()
        count = len(rows)
        return count
    
# TODO:
# Document database class and document model class
# Type cast all new methods and methods missed
# If method returns False, then store the api hashmap in the db
# Replace SQL statements with Pony
# Bug: length of api and length of table not a true measure of equality. ie. new user signs in with the same number of vocab words as a previous user
# Rerun Pydoc
# Create Mock object for tests
# Create getter and setters for model

'''
try:
    con = sqlConn()
    entries = {'casa' : 'house', 'bien' : 'good', 'hermano' : 'brother', 'azul' : 'blue', 'madre' : 'mother'}
    createTable(con)
    hashToTable(con, entries)
    count = numOfEntries(con)
    print (count)
    wordHash = tableToHash(con)
    print (wordHash)
    
finally:
    con.close()
'''