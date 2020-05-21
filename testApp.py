#!/usr/bin/python3

import nose
from app.model import Model

class TestClass:
    """
        Class that orchestrates the tests for the model, view, and controller
    """
    def __init__(self):
        self.model = Model()
    
    """
        Test Suite 1
        
        def test_vocabFlag(self):
            flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
            assert self.model.vocabFlag(flagHash) == False
    
    """
    
    def test_storeUserCredentials1(self):
        self.model.storeUserCredentials("joedane16", "doeisthedear")
        answer = "joedane16"
        assert self.model.username == answer
    
    def test_storeUserCredentials2(self):
        self.model.storeUserCredentials("joedane16", "doeisthedear")
        answer = "doeisthedear"
        assert self.model.password == answer
    
    def test_updateVocabHash(self):
        vocabHash = {'sombrero' : 'hat', 'casa' : 'house', 'gato' : 'cat'}
        flagHash = {'sombrero' : 0, 'casa' : 0, 'gato' : 0}
        answer = {'sombrero' : 'hat', 'casa' : 'house', 'gato' : 'cat'}
        assert self.model.updateVocabHash(vocabHash, flagHash) == answer
    
    def test_updateVocabHash2(self):
        vocabHash = {'sombrero' : 'hat', 'casa' : 'house', 'gato' : 'cat'}
        flagHash = {'sombrero' : 1, 'casa' : 1, 'gato' : 0}
        answer = {'gato' : 'cat'}
        assert self.model.updateVocabHash(vocabHash, flagHash) == answer
    
    def test_vocabFlag(self):
        flagHash = {'sombrero' : 0, 'casa' : 0, 'gato' : 0}
        answer = False
        assert self.model.vocabFlag(flagHash) == answer
    
    def test_vocabFlag2(self):
        flagHash = {'sombrero' : 1, 'casa' : 0, 'gato' : 0}
        answer = False
        assert self.model.vocabFlag(flagHash) == answer
    
    def test_vocabFlag3(self):
        flagHash = {'sombrero' : 1, 'casa' : 1, 'gato' : 1}
        answer = True
        assert self.model.vocabFlag(flagHash) == answer
   
    def test_invertWordHash(self):
        self.model.wordHash = {'sombrero' : 'hat', 'casa' : 'house', 'gato' : 'cat'}
        answer = {'hat' : 'sombrero', 'house' : 'casa', 'cat' : 'gato'}
        assert self.model.invertWordHash() == answer
    
   