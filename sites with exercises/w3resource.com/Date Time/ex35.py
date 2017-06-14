import datetime

today = datetime.date.today().isocalendar()
print(today)

print("Year: {}, number of week: {}, day of a week: {}.".format(*today))