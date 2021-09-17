#
# Example file for working with filesystem shell modules
#
import os
from os import path
import shutil # This is the shell utilities module of python
from shutil import make_archive
from zipfile import ZipFile

def main():
    # Make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # Get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        # Let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # Copy over the permissions, modification times, and other info
        # shutil.copy(src, dst) # This copy function is used to copy the contents of the original file into the new file
        # shutil.copystat(src, dst) # This function is used to copy the metadata from the original file into the new file

        # Rename the original file
        # os.rename("newfile.txt", "newfile.txt") # The rename() function renames the file with the first argument as the name to the second argument

        # # Now put things into a ZIP archive
        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive", "zip", root_dir)

        # More fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:  # 'with' - This is an object constructor
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")
    
if __name__ == "__main__":
    main()