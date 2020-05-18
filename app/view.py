#!/usr/bin/python3

import typing
import getpass
import typing
from typing import List, Dict

class View:
    """
        Class that orchestrates the interactions between program and the terminal
        
    """
    def __init__(self) -> None:
        pass
        
    def display(self) -> bool:
        """
            Method that displays the opening dialogue of the program
            
        """
        print ("welcome to duo terminal: review duolingo words on your terminal...")
        resp = None
        while (resp != 'l'): # repeat loop until the user enters 'l' or 'q'
            resp = (getpass.getpass("select: (L)ogin or (Q)uit \n")).lower()
            if resp == "l": # 'l' for login
                return True
            elif resp == "q": # 'q' for login
                return False
            else:
                print ("(L)ogin or (Q)uit...")
    
    def displayWord(self, word: str) -> str:
        """
            Method that displays the foreign word to the terminal, and retrieves user input
            
        """
        print ("what is the translation of the word?")
        print (word)
        input_ = input().lower() # store the user input in the variable
        return input_
        
    def displayOutput(self, output: str) -> None:
        """
            Method that displays input without any modifications
            
        """
        print (output)
        
    def displayInput(self) -> str:
        """
            Method that securely retrieves user input from user
            
        """
        input_ = (getpass.getpass("\n")).lower() # securely store the user input in the variable
        return input_
    
    def getUserCredentials(self) -> List[str]:
        """
            Method that securely stores user's given username and password
            
        """
        username = getpass.getpass("enter username... \n") # python library that securely stores user input
        password = getpass.getpass("enter password... \n")
        credentials = [username, password]
        return credentials