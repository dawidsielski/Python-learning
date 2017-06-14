import time
import datetime
print(time.asctime(time.strptime('2015 0 0', '%Y %W %w')))


for week_number in range(52):
    time_str = time.strptime('2015 ' + str(week_number) + ' 0', '%Y %W %w')
    sunday = (datetime.date(time_str.tm_year, time_str.tm_mon, time_str.tm_mday))
    print(time.asctime(time_str))