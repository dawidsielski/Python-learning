import datetime

now = datetime.datetime.now()

time_shift = datetime.timedelta(seconds = 5)
print(now.time())

print((now + time_shift).time())