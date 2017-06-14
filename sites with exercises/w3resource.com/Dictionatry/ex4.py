d = {1:10, 2:20}
print(d)

def if_key(key):
    if key in d:
        print("Key in d")
    else:
        print("Key not in d")

if_key(1)
if_key(3)