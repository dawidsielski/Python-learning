from person import *
import shelve
database = shelve.open("persondb")

for element in database:
    print("{} \t=> {}".format(element, database[element]))