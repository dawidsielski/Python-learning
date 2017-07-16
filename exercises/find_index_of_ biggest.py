def solution(A):
    N = len(A)
    result = 0
    for i in range(N):
        for j in range(N):
            if A[i] == A[j]:
                result = max(result, abs(i - j))
    return result


print(solution([6, 2, 6, 4, 5, 6, 5]))