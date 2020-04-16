#!/usr/bin/python3
import sys
import getpass
import duolingo

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def run(self):
        flag = self.view.display()
        if flag == True:
            self.model.userCredentials()
            self.model.signIn()
        else:
            self.exit()
    
    def exit(self):
        print ("until next time...")
        sys.exit()
        

class Model:
    def __init__(self):
        self.username = None
        self.password = None
        self.session = None
    
    def userCredentials(self):
        print ("enter Credentials: ")
        self.username = getpass.getpass("username: ")
        self.password = getpass.getpass("password: ")
    
    def signIn(self):
        print ("signing into duolingo with credentials... ")
        self.session = duolingo.Duolingo(self.username, self.password)
        print (self.session.get_user_info())
    
    
class View:
    def __init__(self):
        pass
        
    def display(self):
        print ("welcome to duo terminal: review duolingo words on your terminal")
        resp = (input("select: (l)ogIn or (q)uit \n")).lower()
        if resp== "l":
            return True
        elif resp == "q":
            return False
    

app = Controller()
app.run()