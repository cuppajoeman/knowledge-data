#!/bin/bash
# We call this script from the root
raw=$(grep $1 kgbase_data/tables.txt)
echo $raw
echo $raw | sed s/.*row-// | sed s/\'.*//

