import pandas as pd
import os

script_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_path, "Cities.csv")) as csv_file:
    read = pd.read_csv(csv_file)


print(read)
print("print the beginning:\n", read.head())
print("print the tail:\n", read.tail())

print(read.sort_values(by=['country','temperature'],ascending=[True,False]))

print(read.city)