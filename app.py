#!/usr/bin/python3

import sys
import getpass
import copy
import duolingo
import hyper
from googletrans import Translator

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def run(self):
        flag = self.view.display()
        if flag == True:
            self.model.userCredentials()
            self.model.signIn()
            self.model.pullVocab()
            self.model.translateToHash()
            self.iterateVocabHash()
            print (self.model.flagHash)
        else:
            self.exit()
    
    def iterateVocabHash(self):
        vocabHash = copy.deepcopy(self.model.wordHash)
        flag = self.model.vocabFlag()
        while flag != True:
            for key in vocabHash:
                input_ = self.view.displayWord(key)
                value = vocabHash[key]
                self.model.compareInput(key, value, input_)
            vocabHash = self.model.updateVocabHash(vocabHash)
            flag = self.model.vocabFlag()
    
    def exit(self):
        print ("until next time...")
        sys.exit()
        
class Model:
    def __init__(self):
        self.username = None
        self.password = None
        self.session = None
        self.vocab = []
        self.wordHash = {}
        self.flagHash = {}
    
    def userCredentials(self):
        print ("enter credentials... ")
        self.username = getpass.getpass("username: ")
        self.password = getpass.getpass("password: ")
    
    def signIn(self):
        try:
            print ("signing into duolingo with credentials... ")
            self.session = duolingo.Duolingo(self.username, self.password)
            print ("signin successful!")
        except:
            print ("signin unsuccessful...")
            print ("try again!")
            self.userCredentials()
            self.signIn()
            
    def pullVocab(self):
        self.vocab = self.session.get_known_words('es')
        self.vocab = self.vocab[:5] # TO SPEED UP DEVELOPMENT: REMOVE LATER!
        print (self.vocab)
    
    def translateToHash(self):
        translator = Translator()
        translations = translator.translate(self.vocab)
        for translation in translations:
            self.wordHash[translation.origin] = translation.text.lower()
            self.flagHash[translation.origin] = 0
    
    def updateVocabHash(self, vocabHash):
        listKnownWords = [key  for (key, value) in self.flagHash.items() if value == 1]
        filteredVocabHash = {key : value for (key, value) in vocabHash.items() if key not in listKnownWords}
        return filteredVocabHash
        
    def compareInput(self, key, value, input_):
        if input_ == value:
            self.flagHash[key] = 1
        return None
    
    def giveWordGetInput(self, hashmap):
        value = hashmap[key]
        input_ = self.view.displayWord(key)
        return input_
        
    def vocabFlag(self):
        if 0 in self.flagHash.values():
            return False
        return True
            
class View:
    def __init__(self):
        pass
        
    def display(self):
        print ("welcome to duo terminal: review duolingo words on your terminal")
        resp = (input("select: (l)ogin or (q)uit \n")).lower()
        if resp== "l":
            return True
        elif resp == "q":
            return False
    
    def displayWord(self, key):
        print ("what is the english translation of the word? ")
        print (key)
        input_ = input().lower()
        return input_
        
        
        
app = Controller()
app.run()