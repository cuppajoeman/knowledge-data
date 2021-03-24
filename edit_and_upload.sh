#!/bin/bash

# Input is a name of the file without the extension
vim $1.tex

# Compile it to pdf
latexmk -pdf $1.tex

# Remove excess files
sh ./cleaner.sh

# Update kgbase tables
python3 kgbase_data/update_kg_table.py && echo tables updated

# Refresh arguments file
sh ./kgbase_data/reset_argfile.sh

# open tables and arguments file
vim -O kgbase_data/arguments.txt kgbase_data/tables.txt

# push data to online
python3 content_to_knowledge_graph.py $1

# push to github
git add -A && git commit && git push
