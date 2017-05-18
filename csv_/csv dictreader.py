import csv
import os

script_path = os.path.dirname(os.path.abspath(__file__))
print(script_path)

airtravel_file = open(os.path.join(script_path, "airtravel.csv"))

rows = csv.DictReader(airtravel_file)
for row in rows:
    print(row)

print(dir(rows))
airtravel_file.close()