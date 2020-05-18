#!/usr/bin/python3

import sys
import typing
from typing import List, Dict
from app.model import Model
from app.view import View

class Controller:
    """
        Class that orchestrates the interactions between model(data) and view(user)
        
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def run(self) -> None:
        """
            Method is the main method that orchestrates all the methods in the model, view, and controller
            
        """
        run = self.view.display() # if the user selects to procede, then with the main program
        if run == True:
            self.storeCredentials() # gets the credentials from the user and store in class methods
            self.storeSession() # gets the credentials to sign into duolingo via api, and then gets the user session and stores it in class method
            if self.model.compareApiToTable() == True:
                print ("getting data from table...")
                # TODO: Create method in model to interact with db
                self.dataToTable()
            else:
                print ("getting data from api...")
                self.dataToModel() # gets the user's data from duolingo via api, and stores the data in the model api
            hashes = self.branchOutput() # gets the user's input to determine the batch of methods used in program
            wordHash = hashes[0] # unpack the two dictionaries
            flagHash = hashes[1]
            self.iterateVocabHash(wordHash, flagHash)
            self.model.closeDb()
        else:
            self.exit()
            
    def storeCredentials(self) -> None:
        """
            Method that obtains from user duolingo credentials and stores it in the model
            
        """
        cred = self.view.getUserCredentials() # get the user credentials
        self.model.storeUserCredentials(cred[0], cred[1])
    
    def storeSession(self) -> None:
        """
            Method that obtains from user duolingo credentials and stores it in the model
            
        """
        self.view.displayOutput("signing into duolingo with credentials... ")
        session = self.model.signIn() # given provided user credentials, attempt login into duolingo
        if session is None:
            self.repeatStoreSession() # the loop will repeat until valid credentials are given and signin succeeds
        self.view.displayOutput("signin successful!")
    
    def repeatStoreSession(self) -> None:
        """
            Method that obtains from user duolingo credentials and stores it in the model
            
            Similar to the storeSession method, but it contains additional print statements
            
        """
        self.view.displayOutput("signin unsuccessful...")
        self.view.displayOutput("try again!")
        self.storeCredentials() # see method for details
        self.storeSession() # see method for detials
    
    def dataToModel(self) -> None:
        """
            Method that orchestrates obtaining from duolingo vocabulary words and converts the words from a list to a hashmap
            
        """
        self.view.displayOutput("obtaining vocabulary...")
        self.model.pullVocab() # store the vocab words in a list
        self.model.translateToHash() # translates the vocab words in a list into a dictionary/ hashmap
    
    def dataToTable(self) -> None:
        """
            Method that orchestrates obtaining from duolingo vocabulary words and converts the words from a list to a hashmap
            
        """
        self.view.displayOutput("loading data...")
        self.model.queryHashFromTable()
        keys = list(self.model.getWordHash().keys())
        flagHash = self.model.makeNewFlagHash(keys)
        self.model.setFlagHash(flagHash)
    
    def branchOutput(self) -> List[Dict]:
        """
            Method that obtains user input. The input determines the batch of methods that are run
            
        """
        self.view.displayOutput("(T)arget to English, or (E)nglish to Target? \n")
        resp = self.view.displayInput()
        if (resp == "t"):
            wordHash = self.model.wordHash # store as is
            flagHash = self.model.flagHash # store as is
        elif (resp == "e"):
            wordHash = self.model.invertWordHash() # reverse the order of keys and values
            flagHash = self.model.makeNewFlagHash(wordHash.keys()) # remake the flagHash variable, but with English words as the key
        hashes = [wordHash, flagHash] # return the two dictionaries in a list
        return hashes
    
    def iterateVocabHash(self, wordHash: Dict[str, str], flagHash: Dict[str, int]) -> None:
        """
            Method orchestrates the interactions between the model(data) and view(user)
            
            Flag is a boolean variable; it releases the program loop if the user translates all of the words
            For loop repeats without the correctly translated words
            
        """
        flag = self.model.vocabFlag(flagHash) # boolean variable: default value is False
        while flag != True:
            for key in wordHash:
                self.vocabIO(key, wordHash, flagHash) # give and get data from the view and model, respectively
            wordHash = self.model.updateVocabHash(wordHash, flagHash) # filter the vocabHash with the translated words
            flag = self.model.vocabFlag(flagHash) # if all words are translated correctly, then update the flag variable
            self.displayNumCorrect(flagHash) # print to the view the number of remaining unlearned words
    
    def displayNumCorrect(self, flagHash: Dict[str, int]) -> None:
        """
            Method that computes and displays the number of remaining words unlearned
            
        """
        numCount = self.model.getNumCorrect(flagHash) # see method for detials
        self.view.displayOutput("Number remaining: {} ".format(len(flagHash) - numCount)) # the computation gives the number of unlearned words
    
    def vocabIO(self, key: str, wordHash: Dict[str, str], flagHash: Dict[str, int]) -> Dict[str, int]:
        """
            Method that displays the vocab word to the view and obtains the translation input from the user
            It also compares the user translation and recorded translation with the compareInput method
            
        """
        input_ = self.view.displayWord(key) # gives the vocab word to the view, and gets the input translation from the user
        value = wordHash[key] # get the translation of the vocab word
        flagHash = self.model.compareInput(key, value, input_, flagHash) # if user input is the same as translation, then stores 1 in flaghashmap; otherwise 0
        return flagHash
        
    def exit(self) -> None:
        """
            Method that safely exits the program
            
        """
        self.view.displayOutput("until next time...")
        sys.exit()