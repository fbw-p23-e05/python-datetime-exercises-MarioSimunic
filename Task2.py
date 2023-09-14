from datetime import datetime, timedelta
current_datetime = datetime.now()

yesterday = current_datetime - timedelta(days=1)
yesterday = yesterday.strftime("%Y %m %d")
today = current_datetime.strftime("%Y %m %d")
tomorrow = current_datetime + timedelta(days=1)
tomorrow = tomorrow.strftime("%Y %m %d")

print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow: ", tomorrow)