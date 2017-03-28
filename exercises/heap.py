import heapq

l = [1,7,3,0,2,87,23,65,34,89,2]
print(heapq.nlargest(2, l))
print(heapq.nsmallest(2, l))

h = []

heapq.heappush(h, (1, "Dawid"))
heapq.heappush(h, (2, "Ilona"))
heapq.heappush(h, (5, "Marta"))
heapq.heappush(h, (4, "Tomasz"))
heapq.heappush(h, (3, "Jacek"))

print(h)

print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(h)