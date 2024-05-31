#!/usr/bin/env python3
import os
import subprocess

# Define the function to get free disk space
def free_space():
    # Launch the Linux command: df -h | grep '/$' | awk '{print $4}' as a new process
    df_command = "df -h | grep '/$' | awk '{print $4}'"
    
    # Execute the command using os.popen()
    output = subprocess.Popen(df_command, shell=True, stdout=subprocess.PIPE)
    
    # Read the output and strip newline characters
    result = output.communicate()[0].decode('utf-8').strip()
    
    # Return the result
    return result

# If the script is executed directly, call the free_space() function
if __name__ == "__main__":
    print(free_space())
