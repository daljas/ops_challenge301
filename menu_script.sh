#!/bin/bash

# Script Name:                  menu_script.sh
# Author:                       Your Name
# Date of latest revision:      12/01/2023
# Purpose:                      A simple menu system in Bash

# Declaration of variables

# Declaration of functions

# Main
while true; do
    # Display menu
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    # Get user input
    read -p "Enter your choice (1-4): " choice

    # Evaluate user input
    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1  # Ping the loopback address
            ;;
        3)
            ifconfig  # Display network adapter information (may need sudo)
            ;;
        4)
            echo "Exiting program. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 4."
            ;;
    esac

    # Prompt to continue
    read -p "Press Enter to continue..."
    clear  # Clear the screen for better visibility
done

# End
