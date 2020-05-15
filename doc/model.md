Module model
============

Classes
-------

`Model()`
:   Class that contains the methods that interact with the 'backend' and data of the program

    ### Methods

    `compareInput(self, key: str, value: str, input_: str, flagHash: Dict[str, int]) -> Dict[str, int]`
    :   Method that compares user input with value (translation) in flagHash

    `getNumCorrect(self, flagHash: Dict[str, int]) -> int`
    :   Method that computes and returns the number of unlearned words remaining

    `invertWordHash(self) -> Dict[str, str]`
    :   Method that switches the pair order of keys and values in a hashmap. Keys -> Values. Values -> Keys

    `makeNewFlagHash(self, keys: List[int]) -> Dict[str, int]`
    :   Method that creates a new flag hashmap

    `pullVocab(self) -> NoneType`
    :   Method that retreives learned words from duolingo stores user's learned words in a list

    `signIn(self) -> <built-in function any>`
    :   Method that returns user session for duolingo user

    `storeUserCredentials(self, username: str, password: str) -> NoneType`
    :   Method that securely stores user's given username and password

    `translateToHash(self) -> NoneType`
    :   Method that converts vocabList into a hashmap (english -> foreign), and another hashmap with key mapped to default value of zero

    `updateVocabHash(self, vocabHash: Dict[str, str], flagHash: Dict[str, int]) -> Dict[str, str]`
    :   Method that filters out learned words from vocabHash

    `vocabFlag(self, flagHash: Dict[str, int]) -> bool`
    :   Method that returns True if all words are translated correctly by the user
