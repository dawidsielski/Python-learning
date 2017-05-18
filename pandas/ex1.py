import pandas as pd
import os

script_path = os.path.dirname(os.path.abspath(__file__))

csv_file = open(os.path.join(script_path, "Cities.csv"))

read = pd.read_csv(csv_file)
print(read)


csv_file.close()