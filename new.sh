#!/bin/bash

# Example ./new defn title
cp $1.tex $2.tex

no_spaces=$(echo "$2" | tr _ " ")

# Rename the title in the latex file and edit it (open the wikibackup too)
sed -i "s/TITLE/$no_spaces/" $2.tex && vim -O $2.tex wikibackup

# Compile it to pdf
latexmk -pdf $2.tex

# Remove excess files
sh ./cleaner.sh

# Update kgbase tables
python3 kgbase_data/update_kg_table.py && echo tables updated

# Refresh arguments file
sh ./kgbase_data/reset_argfile.sh

# open tables and arguments file
sed -i "s/X/$no_spaces/" kgbase_data/arguments.txt
vim -O kgbase_data/arguments.txt kgbase_data/tables.txt

# push data to online
python3 content_to_knowledge_graph.py $2

# push to github
git add -A && git commit && git push
