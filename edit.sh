#!/bin/bash
vim $1 
latexmk -pdf $1
sh ./cleaner.sh
git add -A && git commit && git push
