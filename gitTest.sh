#!/bin/bash
# a script that runs test and adds changes to git commit
# its a debugging script for the developer
# that wants to review the code changes before pushing to origin

echo Running Tests...
pipenv run nosetests testApp.py
echo Adding to Git Staged...
git add --all
git diff --staged