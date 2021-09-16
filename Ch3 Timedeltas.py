#
# Example file for working wtih timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta # timedelta is a span of time

# Construct a basic timedelta and import it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("Today is: ",str(now))

# print today's date one year from now
print("One year from now it will be: "+str(now+timedelta(days=365)))

# Create a timedelta that uses more than one argument
print("In 2 days and 3 weeks it will be: "+str(now+timedelta(days=2, weeks=3)))

# Calculate the date 1 week ago formatted as a string
t = datetime.now()-timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was "+s)

### How many days until April Fools' Day
today = date.today()
afd = date(today.year, 4, 1)

# Use date comparison to see if April Fools' Day has already gone by this year
# If it has, use the replace() function to get the date for next year
if afd<today:
    print("April Fools' Day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year+1)

#Now calculate the amount of time until the next April Fools' Day
    time_to_afd = afd-today
    print("It's just ",time_to_afd.days, "days until April Fools' Day.")