#!/usr/bin/python3

import sys
from app.model import Model
from app.view import View

class Controller:
    """
        Class that orchestrates the interactions between model(data) and view(user)
        
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def run(self):
        """
            Method is the main method that orchestrates all the methods in the model, view, and controller
            
        """
        run = self.view.display() # if the user selects to procede, then with the main program
        if run == True:
            self.storeCredentials()
            self.storeSession()
            self.dataToModel()
            hashes = self.branchOutput()
            wordHash = hashes[0]
            flagHash = hashes[1]
            self.iterateVocabHash(wordHash, flagHash)
        else:
            self.exit()
            
    def storeCredentials(self):
        """
            Method that obtains from user duolingo credentials and stores it in the model
            
        """
        cred = self.view.getUserCredentials()
        self.model.storeUserCredentials(cred[0], cred[1])
    
    def storeSession(self):
        """
            Method that obtains from user duolingo credentials and stores it in the model
            
        """
        # given provided user credentials, attempt login into duolingo
        self.view.displayOutput("signing into duolingo with credentials... ")
        session = self.model.signIn()
        if session is None:
            self.repeatStoreSession()
        self.view.displayOutput("signin successful!")
    
    def repeatStoreSession(self):
        """
            Method that obtains from user duolingo credentials and stores it in the model
            
            Similar to the storeSession method, but it contains additional print statements
            
        """
        self.view.displayOutput("signin unsuccessful...")
        self.view.displayOutput("try again!")
        self.storeCredentials()
        self.storeSession()
    
    def dataToModel(self):
        """
            Method that orchestrates obtaining from duolingo vocabulary words and converts the words from a list to a hashmap
            
        """
        self.view.displayOutput("obtaining vocabulary...")
        self.model.pullVocab()
        self.model.translateToHash()
    
    def branchOutput(self):
        """
            Method that obtains user input. The input determines the batch of methods that are run
            
        """
        self.view.displayOutput("(T)arget to English, or (E)nglish to Target? \n")
        resp = self.view.displayInput()
        if (resp == "t"):
            wordHash = self.model.wordHash
            flagHash = self.model.flagHash
        elif (resp == "e"):
            wordHash = self.model.invertWordHash()
            flagHash = self.model.makeNewFlagHash(wordHash.keys())
        hashes = [wordHash, flagHash]
        return hashes
        
    
    def iterateVocabHash(self, wordHash, flagHash):
        """
            Method orchestrates the interactions between the model(data) and view(user)
            
            Flag is a boolean variable; it releases the program loop if the user translates all of the words
            For loop repeats without the correctly translated words
            
        """
        flag = self.model.vocabFlag(flagHash) # boolean variable: default value is False
        while flag != True:
            for key in wordHash:
                self.vocabIO(key, wordHash, flagHash)
            wordHash = self.model.updateVocabHash(wordHash, flagHash) # filter the vocabHash with the translated words
            flag = self.model.vocabFlag(flagHash) # if all words are translated correctly, then update the flag variable
            self.displayNumCorrect(flagHash)
    
    def displayNumCorrect(self, flagHash):
        """
            Method that computes and displays the number of remaining words unlearned
            
        """
        numCount = self.model.getNumCorrect(flagHash)
        self.view.displayOutput("Number remaining: {} ".format(len(flagHash) - numCount))
    
    def vocabIO(self, key, wordHash, flagHash):
        """
            Method that displays the vocab word to the view and obtains the translation input from the user
            It also compares the user translation and recorded translation with the compareInput method
            
        """
        input_ = self.view.displayWord(key) # gives the vocab word to the view, and gets the input translation from the user
        value = wordHash[key]
        flagHash = self.model.compareInput(key, value, input_, flagHash) # if user input is the same as translation, then stores 1 in flaghashmap; otherwise 0
        return flagHash
        
            
    def exit(self):
        """
            Method that safely exits the program
            
        """
        self.view.displayOutput("until next time...")
        sys.exit()