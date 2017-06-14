import datetime
today = datetime.datetime.now()
print(today)
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)

d1 = datetime.datetime(2017,1,1)
d2 = datetime.datetime(2017,1,15)
print((d2 - d1).days)