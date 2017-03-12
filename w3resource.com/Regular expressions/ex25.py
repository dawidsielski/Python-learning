import re

url = "example.com/users/start=01-01-2012&end=01-31-2012"

def find_date(url):
    dates = re.findall(r'(\d{2})-(\d{2})-(\d{4})',url)
    fixed_dates = []
    for element in dates:
        # fixed_dates.append(element[2] + "-" + element[1] + "-" + element[0])
        fixed_dates.append((element[2], element[1], element[0]))
    print(fixed_dates)


find_date(url)