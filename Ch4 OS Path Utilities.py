#
# Example file for working with os.path module
#

import os # The 'os' module allows us to work with operating-system-related features
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # # Print the name of the OS
    # print(os.name)

    # # Check for item existence and type
    # print("Item exists: "+str(path.exists("textfile.txt"))) # The exist() function specifically checks to see if the file exists
    # print("Item is a file: "+str(path.isfile("textfile.txt"))) # The isfile() function checks to see if the file is a file
    # print("Item is a directory: "+str(path.isdir("textfile.txt"))) # The isdir() function checks to see if the file is a directory

    # # Work with file paths
    # print("Item path: " + str(path.realpath("textfile.txt"))) # The realpath() function returns the full path of the file
    # print("Item path and name: " + str(path.split(path.realpath("textfile.txt")))) # The split() function returns the file name separately with the file path

    # # Get the modification time
    # t = time.ctime(path.getmtime("textfile.txt")) # The getmtime() function gets the modification time of the file
    # print(t)
    # print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) # This returns the time stamp of the modification

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been "+str(td)+" hours since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == "__main__":
    main()