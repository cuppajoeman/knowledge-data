#!/bin/bash

# Example ./new defn title
cp $1.tex $2.tex
sed -i "s/TITLE/$2/" $2.tex
vim $2.tex
sh ./cleaner.sh
git add -A && git commit && git push
