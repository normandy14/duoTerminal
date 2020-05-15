#!/bin/bash

echo Running Tests...
pipenv run nosetests testApp.py
echo Adding to Git Staged...
git add --all
git diff --staged