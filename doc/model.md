Help on module model:

NAME
    model

CLASSES
    builtins.object
        Model
    
    class Model(builtins.object)
     |  Class that contains the methods that interact with the 'backend' and data of the program
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  closeDb(self) -> None
     |      Method that safely closes the database
     |  
     |  compareApiToTable(self) -> bool
     |      Method that compares the number of entries in the user's account with the number of rows in the databse. The program returns a boolean value. True if equal. False otherwise.
     |      
     |      The boolean value represents equality of length
     |  
     |  compareInput(self, key: str, value: str, input_: str, flagHash: Dict[str, int]) -> Dict[str, int]
     |      Method that compares user input with value (translation) in flagHash
     |  
     |  filterDuplHashmap(self, hashmap)
     |      Method that filters/removes entries from a hashmap that have identical key and value. When google translate api cannot find a direct translation, it puts the target language word as the english translation. Thus, the word cannot be correctly translated by the user. Hence, its removal.
     |  
     |  getNumCorrect(self, flagHash: Dict[str, int]) -> int
     |      Method that computes and returns the number of unlearned words remaining
     |      
     |      Bug Note: length of api and length of table not a true measure of equality. ie. new user signs in with the same number of vocab words as a previous user
     |  
     |  getWordHash(self)
     |      Method that returns the value assigned in wordHash
     |  
     |  invertWordHash(self) -> Dict[str, str]
     |      Method that switches the pair order of keys and values in a hashmap. Keys -> Values. Values -> Keys
     |  
     |  makeNewFlagHash(self, keys: List[int]) -> Dict[str, int]
     |      Method that creates a new flag hashmap
     |  
     |  pullVocab(self) -> None
     |      Method that retreives learned words from duolingo stores user's learned words in a list
     |  
     |  queryHashFromTable(self) -> None
     |      Method that converts the rows in the table in the database into a hashmap and assigns the value into a model class variable
     |  
     |  queryHashToTable(self, hashmap) -> None
     |      Method that converts the entries in the hashmap into rows for the table in the database
     |  
     |  recreateTable(self) -> None
     |      Method that deletes and creates a new translation table in the database
     |  
     |  saveDataToPersistentStorage(self) -> None
     |  
     |  setFlagHash(self, hashmap)
     |      Method that assigns the parameter hashmap to the flaghash variable
     |  
     |  signIn(self) -> <built-in function any>
     |      Method that returns user session for duolingo user
     |  
     |  storeUserCredentials(self, username: str, password: str) -> None
     |      Method that securely stores user's given username and password
     |  
     |  translateToHash(self) -> None
     |      Method that converts vocabList into a hashmap (english -> foreign), and another hashmap with key mapped to default value of zero
     |  
     |  updateVocabHash(self, vocabHash: Dict[str, str], flagHash: Dict[str, int]) -> Dict[str, str]
     |      Method that filters out learned words from vocabHash
     |  
     |  vocabFlag(self, flagHash: Dict[str, int]) -> bool
     |      Method that returns True if all words are translated correctly by the user
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

DATA
    Dict = typing.Dict
    List = typing.List

FILE
    /home/normandy14/duoTerminal/app/model.py


