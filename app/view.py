#!/usr/bin/python3

import getpass

class View:
    """
        Class that orchestrates the interactions between program and the terminal
        
    """
    def __init__(self):
        pass
        
    def display(self):
        """
            Method that displays the opening dialogue of the program
            
        """
        print ("welcome to duo terminal: review duolingo words on your terminal...")
        resp = None
        while (resp != 'l'):
            resp = (getpass.getpass("select: (L)ogin or (Q)uit \n")).lower()
            if resp == "l":
                return True
            elif resp == "q":
                return False
            else:
                print ("(L)ogin or (Q)uit...")
    
    def displayWord(self, word):
        """
            Method that displays the foreign word to the terminal, and retrieves user input
            
        """
        print ("what is the translation of the word?")
        print (word)
        input_ = input().lower()
        return input_
        
    def displayOutput(self, output):
        print (output)
        
    def displayInput(self):
        input_ = (getpass.getpass("\n")).lower()
        return input_
    
    def getUserCredentials(self):
        """
            Method that securely stores user's given username and password
            
        """
        username = getpass.getpass("enter username... \n")
        password = getpass.getpass("enter password... \n")
        credentials = [username, password]
        return credentials