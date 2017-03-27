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


#deque
print()

d = collections.deque('dawidd')
print(d)

for character in d:
    print(character.upper(), end = " ")

d.append("aa")
d.appendleft("x")
print(d)

print(d.pop())
print(d)

print(d.popleft())
print(d)

print(list(d))
print(set(d))

print()

print(d)
print(collections.deque(reversed(d)))

print()

print(d)
d.extend('iop')
print(d)

print()

print(d)
d.extendleft('iop')
print(d)