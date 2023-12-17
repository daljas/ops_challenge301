# Author:                   Jason Dallas
# Date of latest revision:  12/17/1986
# Purpose:                  Python with Bash

import os
import subprocess
import time

def snake_bash():
    os.system("clear")
    os.system('figlet "Punching Snakes" -f "3d"')
    print("\n\n")
    time.sleep(1)

    print('LOGGED IN USER:')
    os.system('whoami')
    print("")
    time.sleep(1)

    ip_output = subprocess.getoutput("ip a show eno1 | awk '/inet / {print $2}'")
    print('CURRENT IP ADDRESS:')
    print(ip_output)
    print("")
    time.sleep(1)

    print('THIS PC\'S HARDWARE:')
    os.system('sudo lshw -short')

if __name__ == "__main__":
    snake_bash()
