import collections
d = collections.deque('abcdefg')
print ('Deque:', d)

d.remove('c')
print ('remove(c):', d)

items = [1,2,3,1,2,2,2,1,1,4,85]
my_counter = collections.Counter(items)
print(my_counter)
print(sorted(my_counter.elements()))
print(my_counter.most_common(1))

#subtract

a = collections.deque('aaaxx')
b = collections.deque('aaxx')
c = collections.Counter(a)
d = collections.Counter(b)
print(c.subtract(d))