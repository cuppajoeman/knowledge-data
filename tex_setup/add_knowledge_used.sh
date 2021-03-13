
#!/bin/bash

echo "== Knowledge Used ==" >> "${@: -1}"
for x in "${@:1:$# - 1}" ; do 
  echo "* {{link|target=$x}}" >> "${@: -1}"
done
