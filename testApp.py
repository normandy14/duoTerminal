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
        The following tests suite provides tests coverage for model class only. It ignores any and all methods that interact with
        networking, database, and view
    
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
    
    def test_invertWordHash2(self):
        self.model.wordHash = {'sombrero' : 'hat', 'casa' : 'house', 'gato' : 'cat'}
        answer = {'hat' : 'sombrero', 'house' : 'casa', 'cat' : 'gato'}
        assert self.model.invertWordHash() == answer
    
    def test_makeNewFlagHash(self):
        list_ = ['sombrero', 'casa', 'gato']
        answer = {'sombrero' : 0, 'casa' : 0, 'gato' : 0 }
        self.model.makeNewFlagHash(list_) == answer
    
    def test_compareInput(self):
        flagHash = {'sombrero' : 0, 'casa' : 0, 'gato' : 0 }
        key = 'sombrero'
        value = 'hat'
        input_ = 'hat'
        answer = {'sombrero' : 1, 'casa' : 0, 'gato' : 0 }
        self.model.compareInput(key, value, input_, flagHash) == answer
    
    def test_compareInput2(self):
        flagHash = {'sombrero' : 0, 'casa' : 0, 'gato' : 0 }
        key = 'sombrero'
        value = 'hat'
        input_ = 'pizza'
        answer = {'sombrero' : 0, 'casa' : 0, 'gato' : 0 }
        self.model.compareInput(key, value, input_, flagHash) == answer
    
    def test_getNumCorrect(self):
        flagHash = {'sombrero' : 0, 'casa' : 0, 'gato' : 0 }
        answer = 0
        self.model.getNumCorrect(flagHash) == answer
    
    def test_getNumCorrect2(self):
        flagHash = {'sombrero' : 0, 'casa' : 1, 'gato' : 1 }
        answer = 2
        self.model.getNumCorrect(flagHash) == answer
   
    def test_filterDuplHashmap(self):
        wordHash = {'sombrero' : 'hat', 'casa' : 'house', 'gato' : 'cat'}
        answer = {'sombrero' : 'hat', 'casa' : 'house', 'gato' : 'cat'}
        self.model.filterDuplHashmap(wordHash) == answer
    
    def test_filterDuplHashmap2(self):
        wordHash = {'sombrero' : 'sombrero', 'casa' : 'house', 'gato' : 'goto'}
        answer = {'casa' : 'house'}
        self.model.filterDuplHashmap(wordHash) == answer
