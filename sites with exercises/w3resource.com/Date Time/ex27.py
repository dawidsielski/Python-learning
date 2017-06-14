import datetime

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

date = datetime.date(year, month, day)
offset = datetime.timedelta(days = 20)
print(date)

for times in range(13):
    print(date + offset)
    date = date + offset