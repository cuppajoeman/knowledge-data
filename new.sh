#!/bin/bash

# Example ./new defn title
cp $1.tex $2.tex

# Rename the title in the latex file and edit it
sed -i "s/TITLE/$2/" $2.tex && vim $2.tex

# Compile it to pdf
latexmk -pdf $2.tex

# Remove excess files
sh ./cleaner.sh

# Update kgbase tables
python3 kgbase_data/update_tables.py && echo tables updated

# open tables and arguments file
vim -O kgbase_data/arguments.txt kgbase_data/tables.txt

# push data to online
python3 content_to_knowledge_graph.py

# push to github
git add -A && git commit && git push
