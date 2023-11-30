#!/bin/bash

# Script Name:                  change_permissions.sh
# Author:                       Jason Dallas
# Date of latest revision:      11/30/2023
# Purpose:                      Change permissions of files in a directory

# Declaration of variables
dir_path=""
permissions=""

# Declaration of functions

# Main
read -p "Enter the directory path: " dir_path
read -p "Enter the permissions number (e.g., 777): " permissions

cd "$dir_path" || { echo "Error: Unable to change to directory $dir_path"; exit 1; }

chmod -R "$permissions" .

echo -e "\nDirectory contents:"
ls -l

echo -e "\nNew permissions settings:"
ls -l | awk '{print $1, $9}'

# End
