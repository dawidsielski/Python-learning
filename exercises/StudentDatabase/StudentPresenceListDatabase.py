import shelve
import datetime
import os
import calendar

current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

script_path = os.path.dirname(os.path.realpath(__file__))

if not os.path.isdir(str(current_year)):
    os.mkdir(str(current_year))

os.chdir(str(current_year))

database = shelve.open(str(calendar.month_name[current_month]))

student_id = 193234
student_name = "John Kowalski"

database[str(student_id)] = student_name # can be object type
database.close()