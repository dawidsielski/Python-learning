import datetime

today = datetime.date.today()
offset = datetime.timedelta(days = 30)

print(today - offset)
print(today)
print(today + offset)