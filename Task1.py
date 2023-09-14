from datetime import datetime, timedelta
current_datetime = datetime.now()

# Task 1

print("Current date and time: ", current_datetime)
print("Current year: ", current_datetime.strftime("%Y"))
print("Month of the year: ", current_datetime.strftime("%B"))
print("Week number of the year: ", current_datetime.strftime("%W"))
print("Weekday of the week: ", current_datetime.strftime("%w"))
print("Day of year: ", current_datetime.strftime("%j"))
print("Day of the month: ", current_datetime.strftime("%d"))
print("Day of week: ", current_datetime.strftime("%A"))