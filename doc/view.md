Module view
===========

Classes
-------

`View()`
:   Class that orchestrates the interactions between program and the terminal

    ### Methods

    `display(self)`
    :   Method that displays the opening dialogue of the program

    `displayInput(self)`
    :   Method that securely retrieves user input from user

    `displayOutput(self, output: str)`
    :   Method that displays input without any modifications

    `displayWord(self, word: str)`
    :   Method that displays the foreign word to the terminal, and retrieves user input

    `getUserCredentials(self)`
    :   Method that securely stores user's given username and password
