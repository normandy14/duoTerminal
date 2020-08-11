# DuoTerminal

![Duo](https://vignette.wikia.nocookie.net/duolingo/images/b/be/Duo_2019.png/revision/latest?cb=20190307143704)

DuoTerminal, reinforce learned words that you've learned on the Duolingo web/android/ios platform, all from the convenience of your personal terminal

:brain: Effortlessly Enjoy the learning vocabulary reinforcement process, without even opening a web browser

:pencil2: Translate each word from your target language to English.
Or try your hand at translating from English to your target language. The choice is yours!

:recycle: Continue to translate missed words until you complete the translation cycle.

## Motivation

![App](https://github.com/normandy14/duoTerminal/blob/master/doc/screenshot.png?raw=true)

Duoterminal is a project created for the user that wants to supplement their language learning on the Duolingo platform with additional learning tools. Duolingo is a great learning tool, but its web/android/ios iterface is bulky. The main app also forces user to learn and reinforce learned words in sentences.

DuoTerminal allows for reinforcement of learned words in isolation. It also requires the user to type in by hand the translation of the individual words, unlike the Duolingo app which encourages the user to click the correct translation of a sentence.

## Directory

1. :house: app - contains the *.py files. Central part of app.
2. :file_folder: doc - contains the *.md files. Additional documentation for app.
3. :mailbox_with_mail: sql - contains the *.db files. Rewritable, peripheral) database for app.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

1. :snake: [Python 3](https://www.python.org/) -- Popular Programming Language
2. :snake: [Pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3) -- Programming Packaging Installer
3. :snake: [Pipenv](https://pypi.org/project/pipenv/) -- Programming Enviroment Manager
4. :card_index: [Git](https://git-scm.com/) -- Open Source Distributed Version Control System

Pip3 should be installed before Pipenv because Pip3 is needed to install Pipenv

### Installing

A step by step series of examples that tell you how to get a development env running

1. :card_index: Clone project

```
git clone [(HTTPS/SSH) URL]
```

2. :snake: Enter the Pipenv enviroment

```
pipenv shell
```

3. :snake: Install the program dependencies

```
pipenv install
```

4. :snake: Run the program

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

1. :snake: Enter the shell enviroment

```
pipenv shell
```

2. :snake: Install the dependencies

```
pipenv install --dev
```

3. :snake: Run the tests

```
pipenv run nosetests testApp.py
```

### Break down into end to end tests

Explain what these tests test and why

The tests contained in testApp are unit tests for the Model class.
Methods that involved networking are ommitted (dependency on networking).
Tests on the Controller and View class are ommitted (dependency on user).

The tests test the three following methods:

1. :triangular_flag_on_post: vocabFlag()
2. :triangular_flag_on_post: compareInput()
3. :triangular_flag_on_post: updateVocabHash()

The methods tests the data processing and manipulation of the data stored in hashes

```
pipenv run nosetests testApp.py
----------------------------------------------------------------------
Ran 14 tests in 0.005s

OK
```
<!--

## Deployment

:rocket: Add additional notes about how to deploy this on a live system

-->

## Python Libraries

1. :bird: [Duolingo](https://github.com/KartikTalwar/Duolingo/) -- Unofficial Duolingo API Wrapper
2. :hourglass: [Hyper](https://github.com/python-hyper/hyper/) -- HTTP/2 Client for Python
3. :rainbow: [Google Trans](https://github.com/ssut/py-googletrans/) -- Unofficial Google Translate API Wrapper

## Programming Ideology

This project uses the Model-View-Controller (MVC) paradigm to organize and structure code. The Model-View-Controller paradigm seperates the concerns between the data (model) and display (view). 

1. :robot: Controller - coordinates the interaction between the model and view
2. :microscope: Model - contains the logic of the backend: api and database
3. :art: View - displays the data received by controller to user

## Recommendation for Future Versions of App

Google Trans library is an unoffical api, and we highly recommend for it to be replaced with the official Google Translate service in Google Cloud Platform. However, the offical Google Translate service has a financial cost. It is highly recommended because the unoffical api has poor speed performance. The offical service will signifantly reduce network runtime.

It is also recommended that a graphical api be added such as VueJs or ReactJs.

## Contributing

:newspaper: Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

:card_index: We use [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) for versioning.

## Authors

* :ocean: **Normandy14** - *Initial work* - [Github Account](https://github.com/Normandy14)

## License

:newspaper: This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details

<!--

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

-->
