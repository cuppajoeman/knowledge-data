#!/bin/bash

#find . -type f ! \( -name 'cleaner.sh' -o -name 'scratch[0-9]?.tex' -o -name 'output.txt' \) -delete
find . -type f ! \( -name '.git' -o -name 'cleaner.sh' -o -name 'full_cleaner.sh' -o -name 'add_structure.sh' -o -name '*.tex' -o -name '*.sty' -o -name '*.pdf' -o -name 'new.sh' \) -delete
