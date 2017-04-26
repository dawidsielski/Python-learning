import datetime

start_date = datetime.date(2017,3,3)
end_date = datetime.date(2017,4,26)

offset = datetime.timedelta(days = 1)

while start_date < end_date:
    print(start_date)
    start_date += offset