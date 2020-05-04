#!/usr/bin/python3

import nose
from app import Model

class TestClass:
    """
        Class that orchestrates the tests for the model, view, and controller
    """
    def __init__(self):
        self.model = Model()
    
    """
        Test Suite 1
    
    """
    
    def test_vocabFlag(self):
        self.model.flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
        assert self.model.vocabFlag() == False
    
    def test_vocabFlag2(self):
        self.model.flagHash = {"bien" : 1, "casa" : 1, "tres" : 1}
        assert self.model.vocabFlag() == True
    
    def test_vocabFlag3(self):
        self.model.flagHash = {"bien" : 1, "casa" : 0, "tres" : 1}
        assert self.model.vocabFlag() == False
    
    """
        Test Suite 2
    
    """
        
    def test_compareInput(self):
        self.model.flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
        self.model.compareInput("bien", "bien", "bien")
        assert self.model.flagHash == {"bien" : 1, "casa" : 0, "tres" : 0}
    
    def test_compareInput2(self):
        self.model.flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
        self.model.compareInput("good", "bien", "bien")
        assert self.model.flagHash == {'bien': 0, 'casa': 0, 'tres': 0, 'good': 1}
    
    def test_compareInput3(self):
        self.model.flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
        self.model.compareInput("bien", "good", "bien")
        assert self.model.flagHash == {"bien" : 0, "casa" : 0, "tres" : 0}
    
    """
        Test Suite 3
    
    """
    
    def test_updateVocabHash(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        self.model.flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
        filteredHash = self.model.updateVocabHash(hash_)
        assert filteredHash == {"bien" : "good", "casa" : "house", "tres" : "three"}
    
    def test_updateVocabHash2(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        self.model.flagHash = {"bien" : 1, "casa" : 0, "tres" : 0}
        filteredHash = self.model.updateVocabHash(hash_)
        assert filteredHash == {"casa" : "house", "tres" : "three"}
    
    def test_updateVocabHash3(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        self.model.flagHash = {"bien" : 0, "casa" : 1, "tres" : 0}
        filteredHash = self.model.updateVocabHash(hash_)
        assert filteredHash == {"bien" : "good", "tres" : "three"}
    
    def test_updateVocabHash4(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        self.model.flagHash = {"bien" : 0, "casa" : 0, "tres" : 1}
        filteredHash = self.model.updateVocabHash(hash_)
        assert filteredHash == {"bien" : "good", "casa" : "house"}
    
    def test_updateVocabHash5(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        self.model.flagHash = {"bien" : 1, "casa" : 1, "tres" : 0}
        filteredHash = self.model.updateVocabHash(hash_)
        assert filteredHash == {"tres" : "three"}
    
    def test_updateVocabHash6(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        self.model.flagHash = {"bien" : 1, "casa" : 0, "tres" : 1}
        filteredHash = self.model.updateVocabHash(hash_)
        assert filteredHash == {"casa" : "house"}
        
    def test_updateVocabHash7(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        self.model.flagHash = {"bien" : 0, "casa" : 1, "tres" : 1}
        filteredHash = self.model.updateVocabHash(hash_)
        assert filteredHash == {"bien" : "good"}
    
    def test_updateVocabHash8(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        self.model.flagHash = {"bien" : 1, "casa" : 1, "tres" : 1}
        filteredHash = self.model.updateVocabHash(hash_)
        assert filteredHash == {}