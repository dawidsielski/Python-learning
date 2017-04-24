import datetime

today = datetime.datetime.today().date()
print(today)

time_delta = datetime.timedelta(days = 7)

print(today - time_delta)