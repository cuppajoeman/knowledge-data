#!/bin/bash
shopt -s extglob
#FILES=".git|cleaner.sh|add_structure.sh|*.tex|*.sty|*.pdf|output.txt|new.sh"
#echo !("$FILES")
rm !(.git|cleaner.sh|add_structure.sh|*.tex|*.sty|*.pdf|output.txt|new.sh)
