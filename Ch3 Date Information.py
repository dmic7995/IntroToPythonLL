#
# Example file on working with date information
#

from datetime import date # From the datetime standard module, we want to import the date, time, and datetime classes
from datetime import time # 'date', 'time', and 'datetime' are predefined classes in the python library that lets us manipulate dates and times
from datetime import datetime

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    # today = date.today()
    # print("Today's date is", today)

    # # Print out the date's individual components
    # print("Date components", today.day, today.month, today.year) # These functions return the day, month, and the year stored in the variable 'today'

    # # Retrieve today's weekday (0=Monday, 6=Sunday)
    # print("Today's weekday # is:", today.weekday()) # Weekday() is a FUNCTION, so call it as a function
    # days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    # print("Which is a:", days[today.weekday()])

    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is:", today)

    # Get the current time
    t = datetime.time(datetime.now()) # datetime.time() is a function that calls a constant or a variable and returns something so make sure to put something
                                      # in the brackets
    print(t)

if __name__ == "__main__":
    main()