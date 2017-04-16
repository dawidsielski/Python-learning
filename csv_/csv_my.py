import csv


airtravel_file = open("airtravel.csv")
airtravel = csv.reader(airtravel_file)

for element in airtravel:
    print(element)



print(airtravel)