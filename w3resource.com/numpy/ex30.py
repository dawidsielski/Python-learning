import numpy as np

first_names = ('Margery', 'Betsey', 'Shelley', 'Lanell', 'Genesis')
last_names = ('Woolum', 'Battle', 'Plotner', 'Brien', 'Stahl')
print(last_names)
print(first_names)

print(np.lexsort((first_names, last_names)))