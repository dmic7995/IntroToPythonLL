#
# Example file for working with reading and writing files
#

# You don't need to import any classes for performing these functions - python already knows about these inherently

def main():
    # Open a file for writing and create it if it doesn't exist
    # f = open("textfile.txt", "w+") # The open() function takes two arguments - the file name, 'w' to write in the file,
                                   # and '+' to create the file if it doesn't exist already

    # Open a file for appending text to the end
    f = open("textfile.txt", "r") # 'a' appends data instead of overwriting existing data
                                  # 'r' opens the file for read access
                                  # When appending, make sure that nothing else is done to the file, such as opening and writing for the first time

    # Write some lines of data to the file
    # for i in range(10):
    #     f.write("This is line " +str(i)+ "\r\n") # The write() function writes data to the file

    # Close the file when done
    # f.close()

    # Open the file back up and read the contents
    if f.mode=='r': # This statement checks to see if the file was successfully opened
        # contents = f.read()
        g = f.readlines()
        for x in g:
            print(x)
        # print(contents)

if __name__ == "__main__":
    main()