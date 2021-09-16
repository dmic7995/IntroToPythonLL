#
# Example file for working with calendars
#

# import the calendar module
import calendar # Statement imports all calendar classes from this module

# Create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY) # The part inside the brackets starts the day of the week with the specified day of the week on the printed month
# st = c.formatmonth(2017, 1, 0, 0)
# print (st)

# Create an HTML format calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2017, 1)
# print(abc)

# loop over the days of the month
# zeroes mean that the day of the week is an overlapping month
# for i in c.itermonthdays(2017, 8):
#     print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in full and abbreviated forms
# for name in calendar.month_name:
#     print(name)

# for day in calendar.day_name:
#     print(day)

# Calculate days based on a rule:
# for example, consider a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on: ")
for m in range(1,13):
    cal = calendar.monthcalendar(2018, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY]!=0: # This conditional checks to see if the first Friday of the month is either in the first or second week
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))