"""
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:

alternative text

#Hint: See Fibonacci sequence

#Ref: http://oeis.org/A000045

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.
"""

def perimeter(n):
    fib = [1,1]
    while len(fib) <= n:
        a, b = fib[-1], fib[-2]
        fib.append(a + b)
    # print(sum(fib) * 4)
    return sum(fib) * 4


print(perimeter(5) == 80)
print(perimeter(7) == 216)
print(perimeter(20) == 114624)
print(perimeter(30) == 14098308)
print(perimeter(100) == 6002082144827584333104)