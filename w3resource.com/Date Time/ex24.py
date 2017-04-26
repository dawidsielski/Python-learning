import datetime
"""Print number of mondays between 2015 and 2016"""

date = datetime.date(2015,1,1)

mondays = 0
for year in range(2015, 2017):
    for month in range(1,13):
        if datetime.date(year, month, 1).weekday() == 0:
            mondays += 1
print(mondays)