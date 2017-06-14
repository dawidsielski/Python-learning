import datetime
today = datetime.datetime(2017,7,1,1,1,1)
print(today)
month = (today.month + 6) % 12
six_months = today.replace(month = (month))
print(six_months)