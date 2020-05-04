# DuoTerminal

DuoTerminal, reinforce learned words that you've learned on the Duolingo web/android/ios platform,
all from the convenience of your personal terminal

Effortlessly connect to your Duolingo account without opening a web browser, and enjoy the learning vocabulary reinforcement process!

As you are presented with each word, translate each word from your target language to English.
Or try your hand at translating from English to your target language. The choice is yours!

The words that you missed or repeating until you've completed the translation cycle.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

[Python 3](https://www.python.org/)
[Pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)
[Pipenv](https://pypi.org/project/pipenv/)

Pip3 should be installed before Pipenv because Pip3 is needed to install Pipenv

### Installing

A step by step series of examples that tell you how to get a development env running

1. Install Prerequisites
2. Enter the Pipenv enviroment

```
pipenv shell
```

3. Install the program dependencies

```
pipenv install
```

4. Run the program

```
pipenv run python3 app.py
```

You will be presented with a menu such as the following, when you run the program successfully

```
welcome to duo terminal: review duolingo words on your terminal
select: (l)ogin or (q)uit
```

## Running the tests

Explain how to run the automated tests for this system

1. Enter the shell enviroment

```
pipenv shell
```

2. Install the dependencies

```
pipenv install --dev
```

3. Run the tests

```
pipenv run nosetests testApp.py
```


### Break down into end to end tests

Explain what these tests test and why

The tests contained in testApp are unit tests for the Model class.
Methods that involved networking are ommitted (dependency on networking).
Tests on the Controller and View class are ommitted (dependency on user).


The tests test the three following methods:

  vocabFlag(), compareInput(), updateVocabHash()

The methods tests the data processing and manipulation of the data stored in hashes

```
pipenv run nosetests testApp.py
----------------------------------------------------------------------
Ran 14 tests in 0.005s

OK
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) for versioning.

## Authors

* **Normandy14** - *Initial work* - [Github Account](https://github.com/Normandy14)

## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc