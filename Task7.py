# from datetime import date
# import calendar
# Year= 2023
# A=calendar.TextCalendar(calendar.SUNDAY)
# for b in range(1,13):
#     for k in A.itermonthdays(Year,b):
#         if k!=0:
#             day=date(Year,b,k)
#             if day.weekday()==6:
#                 print("%s,%d-%d-%d" % (calendar.day_name[6] ,k,b,Year))

import datetime

year = int(input("Input a year: "))
date = datetime.date(year, 1, 1)

print("Output:")

while year == date.year:
    if date.weekday() == 6:
        print(date)
    date += datetime.timedelta(1)