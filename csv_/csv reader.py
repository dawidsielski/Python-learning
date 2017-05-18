import csv
import os

script_path = os.path.dirname(os.path.abspath(__file__))
print(script_path)

airtravel_file = open(os.path.join(script_path, "airtravel.csv"))
airtravel = csv.reader(airtravel_file)

for element in airtravel:
    print(element)

airtravel_file.close()