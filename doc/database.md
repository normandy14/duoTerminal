Help on module database:

NAME
    database

CLASSES
    builtins.object
        Database
    
    class Database(builtins.object)
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
     |  createTable(self) -> None
     |      Method that creates a table in the database
     |  
     |  hashToTable(self, hashmap: Dict[str, str]) -> None
     |      Method that converts a hashmap into rows in the table
     |  
     |  numOfEntries(self) -> int
     |      Method that returns the length (number of rows) in the table
     |  
     |  sqlConn(self) -> None
     |      Method that creates a connection to the database
     |  
     |  tableToHash(self) -> Dict[str, str]
     |      Method that converts the rows in the table into a hashmap
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
    /home/normandy14/duoTerminal/app/database.py


