#!/bin/bash

file="output.txt"

#read -p "What is the parent page?: " pp
#read -p "What type of element is this?: " ty

#echo "{{Knowledge Metadata|$pp|$ty}}" >> $file
echo "{{Knowledge Metadata|$1|$2}}" >> $3
