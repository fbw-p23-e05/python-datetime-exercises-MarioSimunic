from datetime import datetime, timedelta
current_datetime = datetime.now()

print("Today: ", current_datetime)

print("Next 5 days:")
for days in range(1, 6):
    print(current_datetime+timedelta(days=days))
    
