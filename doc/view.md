Help on module view:

NAME
    view

CLASSES
    builtins.object
        View
    
    class View(builtins.object)
     |  View() -> None
     |  
     |  Class that orchestrates the interactions between program and the terminal
     |  
     |  Methods defined here:
     |  
     |  __init__(self) -> None
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  display(self) -> bool
     |      Method that displays the opening dialogue of the program
     |  
     |  displayInput(self) -> str
     |      Method that securely retrieves user input from user
     |  
     |  displayOutput(self, output: str) -> None
     |      Method that displays input without any modifications
     |  
     |  displayWord(self, word: str) -> str
     |      Method that displays the foreign word to the terminal, and retrieves user input
     |  
     |  getUserCredentials(self) -> List[str]
     |      Method that securely stores user's given username and password
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
    /home/normandy14/duoTerminal/app/view.py


