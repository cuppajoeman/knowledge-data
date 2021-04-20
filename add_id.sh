#!/bin/bash
# Input: The term that you want an id for, the filename which will be renamed - no extension

grep $1 kgbase_data/tables.txt 

echo "Now copy paste the id you want: (everything after row-)"

read id

# You pass in the file name no extension and then you give the id
mv $2.tex $2-$id.tex
mv $2.pdf $2-$id.pdf
