#!/bin/bash

# Count the number of folders
count=$(find . -maxdepth 1 -type d -not -name '.*' | wc -l)
# Subtract 1 to exclude the current directory (.)
count=$((count - 1))

# Path to the README file
readme_file="README.md"

# Update the README.md file with the current folder count
sed -i "s/Number of questions solved so far:.*/Number of questions solved so far: $count/" $readme_file
