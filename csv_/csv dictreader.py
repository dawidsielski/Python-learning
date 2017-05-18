import csv
import os

script_path = os.path.dirname(os.path.abspath(__file__))
print(script_path)

airtravel_file = open(os.path.join(script_path, "airtravel.csv"))

rows = csv.DictReader(airtravel_file)
for row in rows:
    # print(row)
    for year in range(1958, 1961):
        if row['Month'] == "DEC":
            print(row)

airtravel_file.close()