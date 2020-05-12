#!/usr/bin/python3

import duolingo
import hyper
from googletrans import Translator

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
            