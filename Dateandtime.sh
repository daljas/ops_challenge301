#!/bin/bash

# Script Name:                  dateandtime.sh
# Author:                       Jason Dallas
# Date of latest revision:     
# Purpose:                       Append; Date and Time


# Declaration of variables
source_file="/var/log/syslog"
current_date=$(date +"%Y%m%d%H%M%S")

# Declaration of functions
destination_file="syslog_${current_date}.log"


# Main

cp "$source_file" "$destination_file"


echo "Syslog copied to: $destination_file"


# End of the script
