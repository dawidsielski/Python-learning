def solution(number):
    return sum([x for x in range(1,number) if not x % 3 or not x % 5])


print(solution(10))