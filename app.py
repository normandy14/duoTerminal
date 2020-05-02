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
        print ("What is the English translation of the word? ")
        vocabHash = copy.deepcopy(self.model.wordHash)
        sizeHash = len(vocabHash)
        flag = self.vocabFlag()
        while flag != True:
            for key in vocabHash:
                value = vocabHash[key]
                input_ = self.view.displayWord(key)
                if input_ == value:
                    self.model.flagHash[key] = 1
            flag = self.vocabFlag()
            listKnownWords = [key  for (key, value) in self.model.flagHash.items() if value == 1]
            vocabHash = { key : value for (key, value) in vocabHash.items() if key not in listKnownWords }
            print (listKnownWords)
            print (vocabHash)
    
    def vocabFlag(self):
        if 0 in self.model.flagHash.values():
            return False
        return True
    
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
        print (key)
        input_ = input().lower()
        return input_
        
        
        
app = Controller()
app.run()