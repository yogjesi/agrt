# 23.03.04

def solution(A, B):
    answer = 0
    l = len(A)
    A.sort()
    B.sort(reverse=True)
    for i in range(l):
        answer += A[i]*B[i]
    return answer

result = solution([1,4, 2], [5, 4, 4])
print(result)