import calendar  
year = 2015  
month = 2  
print(calendar.monthrange(year, month))  
print("There are {} days in this month.".format(calendar.monthrange(year, month)[1]))

print(calendar.monthcalendar(year, month))