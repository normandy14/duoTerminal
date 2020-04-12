#!/usr/bin/python3
import sys
import getpass
import duolingo

class Menu:
    """Class to interact with 'view' of the program"""
    
    def __init__(self):
        self.username = None
        self.password = None
        self.session = None
        
    def displayScreen(self):
        """Initial prompt to continue or exit program"""
        
        print ("Welcome to duo terminal: review duolingo words on your terminal")
        resp = (input("Select: (l)ogIn or (q)uit \n")).lower()
        if resp== "l":
            self.getCredentials()
            self.logIn()
        elif resp == "q":
            print ("until next time!")
            sys.exit()
    
    def getCredentials(self):
        """Prompts the user for the username and password of the duolingo account"""
        
        print ("Enter Credentials: ")
        self.username = getpass.getpass("username: ") # getpass records securely sensitive user information
        self.password = getpass.getpass("password: ")
    
    def logIn(self):
        """Uses username and password supplied by user to log into Duolingo and records it into a 'session'"""
        
        print ("signing into duolingo with credentials... ")
        self.session = duolingo.Duolingo(self.username, self.password)
        print (self.session.get_user_info())

menu = Menu()
menu.displayScreen()