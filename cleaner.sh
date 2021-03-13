#!/bin/bash
shopt -s extglob
FILES=".git|cleaner.sh|full_cleaner.sh|add_structure.sh|*.tex|*.sty|*.pdf|output.txt|new.sh"
echo !("$FILES")
