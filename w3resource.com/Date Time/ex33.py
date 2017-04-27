import datetime

d1 = datetime.datetime(2017,1,1,12,12,12)
d2 = datetime.datetime.now()

print((d2 - d1).days)