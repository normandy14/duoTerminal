Help on module controller:

NAME
    controller

CLASSES
    builtins.object
        Controller
    
    class Controller(builtins.object)
     |  Class that orchestrates the interactions between model(data) and view(user)
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  branchGetData(self, lenComp: bool) -> None
     |  
     |  branchOutput(self) -> List[Dict]
     |      Method that obtains user input. The input determines the batch of methods that are run
     |  
     |  dataFromTable(self) -> None
     |      Method that orchestrates obtaining from duolingo vocabulary words and converts the words from a list to a hashmap
     |  
     |  dataToModel(self) -> None
     |      Method that orchestrates obtaining from duolingo vocabulary words and converts the words from a list to a hashmap
     |  
     |  displayNumCorrect(self, flagHash: Dict[str, int]) -> None
     |      Method that computes and displays the number of remaining words unlearned
     |  
     |  exit(self) -> None
     |      Method that safely exits the program
     |  
     |  iterateVocabHash(self, wordHash: Dict[str, str], flagHash: Dict[str, int]) -> None
     |      Method orchestrates the interactions between the model(data) and view(user)
     |      
     |      Flag is a boolean variable; it releases the program loop if the user translates all of the words
     |      For loop repeats without the correctly translated words
     |  
     |  repeatStoreSession(self) -> None
     |      Method that obtains from user duolingo credentials and stores it in the model
     |      
     |      Similar to the storeSession method, but it contains additional print statements
     |  
     |  run(self) -> None
     |      Method is the main method that orchestrates all the methods in the model, view, and controller
     |  
     |  storeCredentials(self) -> None
     |      Method that obtains from user duolingo credentials and stores it in the model
     |  
     |  storeSession(self) -> None
     |      Method that obtains from user duolingo credentials and stores it in the model
     |  
     |  vocabIO(self, key: str, wordHash: Dict[str, str], flagHash: Dict[str, int]) -> Dict[str, int]
     |      Method that displays the vocab word to the view and obtains the translation input from the user
     |      It also compares the user translation and recorded translation with the compareInput method
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
    /home/normandy14/duoTerminal/app/controller.py


