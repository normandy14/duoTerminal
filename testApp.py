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
        flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
        assert self.model.vocabFlag(flagHash) == False
    
    def test_vocabFlag2(self):
        flagHash = {"bien" : 1, "casa" : 1, "tres" : 1}
        assert self.model.vocabFlag(flagHash) == True
    
    def test_vocabFlag3(self):
        flagHash = {"bien" : 1, "casa" : 0, "tres" : 1}
        assert self.model.vocabFlag(flagHash) == False
    
    """
        Test Suite 2
    
    """
        
    def test_compareInput(self):
        flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
        self.model.compareInput("bien", "bien", "bien", flagHash)
        assert flagHash == {"bien" : 1, "casa" : 0, "tres" : 0}
    
    def test_compareInput2(self):
        flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
        self.model.compareInput("good", "bien", "bien", flagHash)
        assert flagHash == {'bien': 0, 'casa': 0, 'tres': 0, 'good': 1}
    
    def test_compareInput3(self):
        flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
        self.model.compareInput("bien", "good", "bien", flagHash)
        assert flagHash == {"bien" : 0, "casa" : 0, "tres" : 0}
    
    """
        Test Suite 3
    
    """
    
    def test_updateVocabHash(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        flagHash = {"bien" : 0, "casa" : 0, "tres" : 0}
        filteredHash = self.model.updateVocabHash(hash_, flagHash)
        assert filteredHash == {"bien" : "good", "casa" : "house", "tres" : "three"}
    
    def test_updateVocabHash2(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        flagHash = {"bien" : 1, "casa" : 0, "tres" : 0}
        filteredHash = self.model.updateVocabHash(hash_, flagHash)
        assert filteredHash == {"casa" : "house", "tres" : "three"}
    
    def test_updateVocabHash3(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        flagHash = {"bien" : 0, "casa" : 1, "tres" : 0}
        filteredHash = self.model.updateVocabHash(hash_, flagHash)
        assert filteredHash == {"bien" : "good", "tres" : "three"}
    
    def test_updateVocabHash4(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        flagHash = {"bien" : 0, "casa" : 0, "tres" : 1}
        filteredHash = self.model.updateVocabHash(hash_, flagHash)
        assert filteredHash == {"bien" : "good", "casa" : "house"}
    
    def test_updateVocabHash5(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        flagHash = {"bien" : 1, "casa" : 1, "tres" : 0}
        filteredHash = self.model.updateVocabHash(hash_, flagHash)
        assert filteredHash == {"tres" : "three"}
    
    def test_updateVocabHash6(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        flagHash = {"bien" : 1, "casa" : 0, "tres" : 1}
        filteredHash = self.model.updateVocabHash(hash_, flagHash)
        assert filteredHash == {"casa" : "house"}
        
    def test_updateVocabHash7(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        flagHash = {"bien" : 0, "casa" : 1, "tres" : 1}
        filteredHash = self.model.updateVocabHash(hash_, flagHash)
        assert filteredHash == {"bien" : "good"}
    
    def test_updateVocabHash8(self):
        hash_ = {"bien" : "good", "casa" : "house", "tres" : "three"}
        flagHash = {"bien" : 1, "casa" : 1, "tres" : 1}
        filteredHash = self.model.updateVocabHash(hash_, flagHash)
        assert filteredHash == {}