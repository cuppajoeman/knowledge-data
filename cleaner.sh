#!/bin/bash
shopt -s extglob nullglob
files=(!(.|..|.gitignore|.git|.env|cleaner.sh|edit.sh|*.tex|*.sty|*.pdf|output.txt|new.sh|kgbase_data|content_to_knowledge_graph.py|README.txt|add_id.sh|edit_and_upload.sh|new_no_upload.sh|wikibackup))

# ${#files[@]} is the number of entries in the file array
if (( ${#files[@]} > 0 )); then
 printf 'files to be deleted:\n'
 printf '%s\n' "${files[@]}"
  # Ask for confirmation
  read -p "Are you sure? " -n 1 -r
  echo    # (optional) move to a new line
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -- "${files[@]}"
  fi
else
 printf 'no files found to be deleted:\n'
fi

# Clean up any accidental files
rm .aux .fdb_latexmk .fls .log
