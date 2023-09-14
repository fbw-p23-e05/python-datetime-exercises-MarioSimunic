from datetime import datetime, timedelta
current_datetime = datetime.now()

print("Today: ", current_datetime)

day = current_datetime.strftime("%j")

print("Day of the year: ", day)