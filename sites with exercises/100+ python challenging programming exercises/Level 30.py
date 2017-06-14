"""line 1071"""

def halfTuple(tup):
    half = int(len(tup) / 2)
    print(tup[:half])
    print(tup[half:])


t = (1,2,3,4,5,6,7,8,9,10)
halfTuple(t)