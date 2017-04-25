import datetime
d = datetime.date.today()
t = datetime.time(0,0,0)

dt = datetime.datetime.combine(d,t)
print(dt)