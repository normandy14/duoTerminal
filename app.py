#!/usr/bin/python3

import sys
import getpass
import duolingo
import hyper
from googletrans import Translator

# TODO:
# 2. Add Python Type Feature
# 3. Seperate MVC into 3 Seperate Files
# 4. Add more Language Support

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
        '''
            Method that obtains from user duolingo credentials and stores it in the model
            
        '''
        cred = self.view.getUserCredentials()
        self.model.storeUserCredentials(cred[0], cred[1])
    
    def storeSession(self):
        # given provided user credentials, attempt login into duolingo
        self.view.displayOutput("signing into duolingo with credentials... ")
        session = self.model.signIn()
        if session is None:
            # repeat the process until the user provides valid credentials
            self.view.displayOutput("signin unsuccessful...")
            self.view.displayOutput("try again!")
            self.storeCredentials()
            self.storeSession()
        self.view.displayOutput("signin successful!")
    
    def dataToModel(self):
        self.view.displayOutput("obtaining vocabulary...")
        
        # obtains learned words from the duolingo account and converts the words into a hashmap (dictionary)
        self.model.pullVocab()
        self.model.translateToHash()
    
    def branchOutput(self):
        # ask if user wants to translate target language into english, or english into target language
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
                
                 # MAKE INTO OWN METHOD (vocabIO)
                input_ = self.view.displayWord(key) # gives the vocab word to the view, and gets the input translation from the user
                value = wordHash[key]
                flagHash = self.model.compareInput(key, value, input_, flagHash) # if user input is the same as translation, then stores 1 in flaghashmap; otherwise 0
                
            # MAKE INTO OWN METHOD (process hashmaps, return flag variable)
            wordHash = self.model.updateVocabHash(wordHash, flagHash) # filter the vocabHash with the translated words
            flag = self.model.vocabFlag(flagHash) # if all words are translated correctly, then update the flag variable
            numCount = self.model.getNumCorrect(flagHash)
            self.view.displayOutput("Number remaining: {} ".format(len(flagHash) - numCount))
            
    def exit(self):
        """
            Method that safely exits the program
            
        """
        self.view.displayOutput("until next time...")
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
            self.session = duolingo.Duolingo(self.username, self.password)
            return False
        except:
            return None
            
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
    
if __name__ == "__main__":
    app = Controller()
    app.run()