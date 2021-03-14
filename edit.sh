#!/bin/bash
vim $1 
sh ./cleaner
git add -A && git commit && git push
