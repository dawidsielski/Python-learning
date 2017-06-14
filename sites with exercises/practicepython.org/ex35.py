import json
import re
import collections

f = open("birthdays.json", "r")
birthdays = json.load(f)
f.close()

dates = []
for element in birthdays.values():
    dates.append(element.split("/")[0])
c = collections.Counter(dates)
print(c['01'])
print(c)