from datetime import date, timedelta
import calendar
start_date = date(2014, 12, 25)
days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
print(start_date + timedelta(days=days_in_month))