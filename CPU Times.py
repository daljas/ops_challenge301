# Script Name:                  CPU Times Information Script
# Author:                       Jason Dallas
# Date of latest revision:      12/23/2023
# Purpose:                      Display CPU times information




import psutil

# Get CPU times information
cpu_times = psutil.cpu_times()

# Print the obtained information
print(f"User Mode Time: {cpu_times.user} seconds")
print(f"Kernel Mode Time: {cpu_times.system} seconds")
print(f"Idle Time: {cpu_times.idle} seconds")
print(f"Priority User Mode Time: {cpu_times.nice} seconds")
print(f"I/O Wait Time: {cpu_times.iowait} seconds")
print(f"Hardware Interrupt Time: {cpu_times.irq} seconds")
print(f"Software Interrupt Time: {cpu_times.softirq} seconds")
print(f"Virtualized OS Time: {cpu_times.steal} seconds")
print(f"Guest OS CPU Time: {cpu_times.guest} seconds")


