#!/usr/bin/python3
import sys
import getpass
import duolingo

class Menu:
    def __init__(self):
        self.username = None
        self.password = None
        self.session = None
        
    def displayScreen(self):
        print ("Welcome to duo terminal: review duolingo words on your terminal")
        resp = (input("Select: (l)ogIn or (q)uit \n")).lower()
        if resp== "l":
            self.getCredentials()
            self.logIn()
        elif resp == "q":
            print ("until next time!")
            sys.exit()
    
    def getCredentials(self):
        print ("Enter Credentials: ")
        self.username = getpass.getpass("username: ")
        self.password = getpass.getpass("password: ")
    
    def logIn(self):
        print ("signing into duolingo with credentials... ")
        self.session = duolingo.Duolingo(self.username, self.password)
        print (self.session.get_user_info())

menu = Menu()
menu.displayScreen()