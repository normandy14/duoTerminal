import sqlite3
from sqlite3 import Error
import typing
from typing import List, Dict

class Database:
    """
        Class that contains the methods that interact with the 'backend' and data of the program
        
    """
        
    def __init__(self):
        self.con = None
        self.cur = None
        self.sqlConn()
        self.createTable() # Make check to see if table already exists!
    
    def sqlConn(self) -> None:
        """
            Method that creates a connection to the database
        
        """
        try:
            self.con = sqlite3.connect('sql/duo.db')
            self.cur = self.con.cursor()
        except Error:
            print (Error)
        
    def createTable(self) -> None:
        """
            Method that creates a table in the database
        
        """
        try:
            self.cur.execute("CREATE TABLE IF NOT EXISTS translation (target text PRIMARY KEY, english text)")
            self.con.commit()
        except Error:
            print (Error)
    
    def dropTable(self) -> None:
        try:
            self.cur.execute("DROP TABLE if EXISTS translation")
            self.con.commit()
        except Error:
            print (Error)

    def hashToTable(self, hashmap: Dict[str, str]) -> None:
        """
            Method that converts a hashmap into rows in the table
        
        """
        try:
            for key, value in hashmap.items():
                self.cur.execute("INSERT INTO translation(target, english) VALUES(?, ?)", (key, value))
                self.con.commit()
        except Error:
            print (Error)

    def tableToHash(self) -> Dict[str, str]:
        """
            Method that converts the rows in the table into a hashmap
        
        """
        wordHash = {}
        self.cur.execute("SELECT target, english FROM translation")
        rows = self.cur.fetchall()
        for row in rows:
            wordHash[row[0]] = row[1] # unpack the row variable
        return wordHash

    def numOfEntries(self) -> int:
        """
            Method that returns the length (number of rows) in the table
        
        """
        self.cur.execute("SELECT target, english FROM translation")
        rows = self.cur.fetchall()
        count = len(rows)
        return count
    
    def closeDb(self) -> None:
        """
            Method that safely closes the database
            
        """
        self.con.close()
    
# TODO:
# Replace SQL statements with Pony
# Create Mock object for tests
