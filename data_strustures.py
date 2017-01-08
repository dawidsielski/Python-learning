l = [1,2,3]

l.append(5)

l.extend([6,7,8])

l.insert(3,4)

l.remove(6)

l.pop(0)

print(l)


from collections import deque
queue = deque(["Dawid", "Mariusz"])

queue.append("Ilona")

print(queue.popleft())
print(queue.pop())

print(queue)


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
a = ([weapon.strip() for weapon in freshfruit])
print(a)


# nested list comprehensions

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]

matrix1 = [[row[i] for row in matrix] for i in range(4)]
print("Marix 1",matrix1)

matrix2 = [[10,20,30,40], [50,60,70,80], [90,100,110,120]]

print("Two nestes list zipped",list(zip(matrix,matrix2)))
