#!/usr/bin/python3

import typing
from typing import List, Dict
import duolingo
import hyper
from googletrans import Translator
from app.database import Database

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
        self.db = Database()
    
    """
        The following methods:
        
            userCredentials(), signIn(), pullVocab(), translateToHash()
        
        Interact with web services using the duolingo package.
        It requires HTTP/s and a network connect to the internet
        
    """
    
    def storeUserCredentials(self, username: str, password: str) -> None:
        """
            Method that securely stores user's given username and password
            
        """
        self.username = username # stores the local variable into the class
        self.password = password # stores the local variable into the class
        
    def signIn(self) -> any:
        """
            Method that returns user session for duolingo user
            
        """
        try:
            self.session = duolingo.Duolingo(self.username, self.password) # stores the user credentials into the duolingo constructor
            return True # boolean value has no meaning; simply differentiate from None
        except:
            return None # used as a marker for conditional statement in the controller class methods its called from
            
    def compareApiToTable(self):
        vocab = self.session.get_known_words('es')[:5] # TO SPEED UP DEVELOPMENT: GENERALIZE LATER!
        countAccount = len(vocab)
        countRows = self.db.numOfEntries()
        if countAccount == countRows:
            return True
        return False
    
    def pullVocab(self) -> None:
        """
            Method that retreives learned words from duolingo stores user's learned words in a list
            
        """
        self.vocab = self.session.get_known_words('es') # TO SPEED UP DEVELOPMENT: GENERALIZE LATER! # used to retrieve list of all learned words that user has learned
        self.vocab = self.vocab[:5] # TO SPEED UP DEVELOPMENT: REMOVE LATER!
    
    def translateToHash(self) -> None:
        """
            Method that converts vocabList into a hashmap (english -> foreign), and another hashmap with key mapped to default value of zero
            
        """
        translator = Translator() # googletrans constructor
        translations = translator.translate(self.vocab) # method of googletrans constructor
        for translation in translations:
            self.wordHash[translation.origin] = translation.text.lower() # store the foreign language word as the key with corresponding english translation
            self.flagHash[translation.origin] = 0 # every word in this dictionary is, by default, unlearned`
    
    def getHashFromTable(self):
        self.wordHash = self.db.tableToHash()
    
    def getWordHash(self):
        return self.wordHash
    
    def setFlagHash(self, hashmap):
        self.flagHash = hashmap
    
    def updateVocabHash(self, vocabHash: Dict[str, str], flagHash: Dict[str, int]) -> Dict[str, str]:
        """
            Method that filters out learned words from vocabHash
            
        """
        listKnownWords = [key  for (key, value) in flagHash.items() if value == 1] # uses the flags in flagHash to determine in word is learned
        filteredVocabHash = {key : value for (key, value) in vocabHash.items() if key not in listKnownWords} # uses the listKnownWords to filter vocabHash so that only unlearned words remained
        return filteredVocabHash
        
    def vocabFlag(self, flagHash: Dict[str, int]) -> bool:
        """
            Method that returns True if all words are translated correctly by the user
            
        """
        if 0 in flagHash.values(): # searches if there are unlearned words in the hashmap
            return False # at first occurence of 0/ if any occurence of 0, return False; meaning of 0: word is unlearned
        return True
    
    """
        The following methods:
        
            invertWordHash(), makeNewFlagHash(), compareInput(), getNumCorrect(),
        
        Are helper methods to the model class. They increase the modularity of the code by seperating
        the procedural operations into small methods.
        

    """
        
    def invertWordHash(self) -> Dict[str, str]:
        """
            Method that switches the pair order of keys and values in a hashmap. Keys -> Values. Values -> Keys
            
        """
        invertHash = {}
        keys = list(self.wordHash.keys()) # put all the keys of the dictionary in a list
        values = list(self.wordHash.values()) # put all the values of the dictionary in a list
        for i in range(len(values)):
            invertHash[values[i]] = keys[i] # swap the values of the keys and values and store in the new dictionary
        return invertHash
        
    def makeNewFlagHash(self, keys: List[int]) -> Dict[str, int]:
        """
            Method that creates a new flag hashmap
            
        """
        flagHash = {}
        for key in keys:
            flagHash[key] = 0 # assign all the keys in the list with the value 0 in the new flagHash variable
        return flagHash
    
    def compareInput(self, key: str, value: str, input_: str, flagHash: Dict[str, int]) -> Dict[str, int]:
        """
            Method that compares user input with value (translation) in flagHash
            
        """
        if input_ == value: # if the user's answer matches the recorded answer in the dictionary
            flagHash[key] = 1 # True, marks a word as learned
        return flagHash
        
    def getNumCorrect(self, flagHash: Dict[str, int]) -> int:
        """
            Method that computes and returns the number of unlearned words remaining
            
        """
        filteredFlagHash = [key for (key, value) in flagHash.items() if value == 1] # remove all the unlearned words
        numCorrect = len(filteredFlagHash) # the number of words that the user translated correctly (learned words)
        return numCorrect
            