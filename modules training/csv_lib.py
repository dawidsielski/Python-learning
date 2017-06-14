import csv

with open('Cities.csv') as csvfile:
     spamreader = csv.reader(csvfile,codec = 'utf8', delimiter=' ', quotechar='|')
     for row in spamreader:
         print(', '.join(row))