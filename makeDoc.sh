#!/bin/bash
# a script that runs generates documentation in the app folder and puts it in the doc folder
# its a script for the developer to create and update documentation
echo Generating Documentation...
arr=(app/*)
for f in "${arr[@]}"; do
  python3 -m pydoc "$f" > doc/${f:4:-3}.md
done

