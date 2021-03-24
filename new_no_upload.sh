#!/bin/bash

# Example ./new defn title
cp $1.tex $2.tex

# Rename the title in the latex file and edit it (open the wikibackup too)
sed -i "s/TITLE/$2/" $2.tex && vim -O $2.tex ../wikibackup

# Compile it to pdf
latexmk -pdf $2.tex

# Remove excess files
sh ./cleaner.sh

# push to github
git add -A && git commit && git push
