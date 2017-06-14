d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}

d1_keys = d1.keys()
d2_keys = d2.keys()

for key in d1_keys:
    if key in d2_keys:
        print("key " + key + " is in d1 and d2")
