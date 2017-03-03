sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
sentence = sentence.split()

unique = []
unique = [x for x in sentence if x not in unique]

frequency = {}
for element in unique:
    frequency[element] = sentence.count(element)

frequency_sorted = sorted(frequency)

for element in frequency_sorted:
    print(str(element) + ":" + str(frequency[element]))