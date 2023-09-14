import time, datetime

mon = time.asctime(time.strptime('2023 37 1', '%Y %W %w'))

print("The first Monday of this week was: ", mon)