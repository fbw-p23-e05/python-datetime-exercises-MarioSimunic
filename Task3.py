from datetime import datetime, timedelta
current_datetime = datetime.now()

new_time = current_datetime+timedelta(seconds=5)

print("Current time: ", current_datetime)
print("After adding 5 seconds: ", new_time)