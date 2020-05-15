Module controller
=================

Classes
-------

`Controller()`
:   Class that orchestrates the interactions between model(data) and view(user)

    ### Methods

    `branchOutput(self) -> List[Dict]`
    :   Method that obtains user input. The input determines the batch of methods that are run

    `dataToModel(self)`
    :   Method that orchestrates obtaining from duolingo vocabulary words and converts the words from a list to a hashmap

    `displayNumCorrect(self, flagHash: Dict[str, int]) -> NoneType`
    :   Method that computes and displays the number of remaining words unlearned

    `exit(self)`
    :   Method that safely exits the program

    `iterateVocabHash(self, wordHash: Dict[str, str], flagHash: Dict[str, int]) -> NoneType`
    :   Method orchestrates the interactions between the model(data) and view(user)
        
        Flag is a boolean variable; it releases the program loop if the user translates all of the words
        For loop repeats without the correctly translated words

    `repeatStoreSession(self)`
    :   Method that obtains from user duolingo credentials and stores it in the model
        
        Similar to the storeSession method, but it contains additional print statements

    `run(self)`
    :   Method is the main method that orchestrates all the methods in the model, view, and controller

    `storeCredentials(self)`
    :   Method that obtains from user duolingo credentials and stores it in the model

    `storeSession(self)`
    :   Method that obtains from user duolingo credentials and stores it in the model

    `vocabIO(self, key: str, wordHash: Dict[str, str], flagHash: Dict[str, int]) -> Dict[str, int]`
    :   Method that displays the vocab word to the view and obtains the translation input from the user
        It also compares the user translation and recorded translation with the compareInput method
