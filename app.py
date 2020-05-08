#!/usr/bin/python3

import sys
import getpass
import copy
import duolingo
import hyper
from googletrans import Translator

# TODO:
# 1. Convert Translation (English to Target) Direction
# 2. Show Number Correct, Number Incorrect
# 3. Expand to More Languages (Get the languages the user has trees for)

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
        flag = self.view.display() # if the user selects to procede, then with the main program
        if flag == True:
            
            # DEBUG: hashmap hardcoded for offline development
            
            '''
            
                cred = self.view.getUserCredentials()
                self.model.storeUserCredentials(cred[0], cred[1])
                self.model.signIn()
                self.model.pullVocab()
                # Important: Delete Later!
            
            '''
            
            self.model.wordHash = {'hola' : 'hello', 'en' : 'in', 'tres' : 'three', 'casa' : 'house', 'ciudad' : 'city'}
            self.model.flagHash = {'hola' : 0, 'en' : 0, 'tres' : 0, 'casa' : 0, 'ciudad' : 0}
            self.model.translateToHash()
            
            wordHash = {}
            resp = (getpass.getpass("(T)arget to English, or (E)nglish to Target? \n")).lower()
            if (resp == "t"):
                wordHash = self.model.wordHash
                flagHash = self.model.flagHash
            elif (resp == "e"):
                wordHash = self.model.invertWordHash()
                flagHash = self.model.makeNewFlagHash(wordHash.keys())
            self.iterateVocabHash(wordHash, flagHash)
            
        else:
            self.exit()
    
    def iterateVocabHash(self, wordHash, flagHash):
        """
            Method orchestrates the interactions between the model(data) and view(user)
            
            Flag is a boolean variable; it releases the program loop if the user translates all of the words
            For loop repeats without the correctly translated words
            
        """
        flag = self.model.vocabFlag(flagHash) # boolean variable: default value is False
        while flag != True:
            for key in wordHash:
                input_ = self.view.displayWord(key) # gives the vocab word to the view, and gets the input translation from the user
                value = wordHash[key]
                flagHash = self.model.compareInput(key, value, input_, flagHash) # if user input is the same as translation, then stores 1 in flaghashmap; otherwise 0
            wordHash = self.model.updateVocabHash(wordHash, flagHash) # filter the vocabHash with the translated words
            
            flag = self.model.vocabFlag(flagHash) # if all words are translated correctly, then update the flag variable
            numCount = self.model.getNumCorrect(flagHash)
            self.view.displayOutput("Number remaining: {} ".format(len(flagHash) - numCount))
            
    def exit(self):
        """
            Method that safely exits the program
            
        """
        print ("until next time...")
        sys.exit()
        
class Model:
    """
        Class that contains the methods that interact with the 'backend' and data of the program
        
    """
    def __init__(self):
        self.username = None
        self.password = None
        self.session = None
        self.vocab = []
        self.wordHash = {}
        self.flagHash = {}
    
    """
        The following methods:
        
            userCredentials(), signIn(), pullVocab(), translateToHash()
        
        Interact with web services using the duolingo package.
        It requires HTTP/s and a network connect to the internet
        
    """
    
    def storeUserCredentials(self, username, password):
        """
            Method that securely stores user's given username and password
            
        """
        self.username = username
        self.password = password
        
    # Printing is done in the Model! Move to Controller and View!
    def signIn(self):
        """
            Method that returns user session for duolingo user
            
        """
        try:
            print ("signing into duolingo with credentials... ")
            self.session = duolingo.Duolingo(self.username, self.password)
            print ("signin successful!")
        except:
            print ("signin unsuccessful...")
            print ("try again!")
            self.storeUserCredentials()
            self.signIn()
            
    def pullVocab(self):
        """
            Method that retreives learned words from duolingo stores user's learned words in a list
            
        """
        self.vocab = self.session.get_known_words('es') # TO SPEED UP DEVELOPMENT: GENERALIZE LATER!
        self.vocab = self.vocab[:5] # TO SPEED UP DEVELOPMENT: REMOVE LATER!
    
    def translateToHash(self):
        """
            Method that converts vocabList into a hashmap (english -> foreign), and another hashmap with key mapped to default value of zero
            
        """
        translator = Translator() # googletrans constructor
        translations = translator.translate(self.vocab) # method of googletrans constructor
        for translation in translations:
            self.wordHash[translation.origin] = translation.text.lower()
            self.flagHash[translation.origin] = 0
    
    """
        The following methods:
        
            translatetoHash(), updateVocabHash(), compareInput(), vocabFlag()
        
        Interact with 'backend' of the program. It processes and interacts with the data pulled from the duolingo package,
        and sends it to the controller class
    
    """
    
    def invertWordHash(self):
        """
            Method that switches the pair order of keys and values in a hashmap. Keys -> Values. Values -> Keys
            
        """
        invertHash = {}
        keys = list(self.wordHash.keys())
        values = list(self.wordHash.values())
        for i in range(len(values)):
            invertHash[values[i]] = keys[i]
        return invertHash
        
    def makeNewFlagHash(self, keys):
        """
            Method that creates a new flag hashmap
            
        """
        flagHash = {}
        for key in keys:
            flagHash[key] = 0
        return flagHash
    
    def updateVocabHash(self, vocabHash, flagHash):
        """
            Method that filters out learned words from vocabHash
            
        """
        listKnownWords = [key  for (key, value) in flagHash.items() if value == 1] # uses the flags in flagHash to determine in word is learned
        filteredVocabHash = {key : value for (key, value) in vocabHash.items() if key not in listKnownWords} # uses the listKnownWords to filter vocabHash
        return filteredVocabHash
        
    def compareInput(self, key, value, input_, flagHash):
        """
            Method that compares user input with value (translation) in flagHash
            
        """
        if input_ == value:
            flagHash[key] = 1 # True, marks a learned word
        return flagHash
    
    def getNumCorrect(self, flagHash):
        filteredFlagHash = [key for (key, value) in flagHash.items() if value == 1]
        numCorrect = len(filteredFlagHash)
        return numCorrect
        
    def vocabFlag(self, flagHash):
        """
            Method that returns True if all words are translated correctly by the user
            
        """
        if 0 in flagHash.values(): # searches if there are unlearned words in the hashmap
            return False
        return True
            
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
    
    def getUserCredentials(self):
        """
            Method that securely stores user's given username and password
            
        """
        username = getpass.getpass("enter username... \n")
        password = getpass.getpass("enter password... \n")
        credentials = [username, password]
        return credentials
    
if __name__ == "__main__":
    app = Controller()
    app.run()