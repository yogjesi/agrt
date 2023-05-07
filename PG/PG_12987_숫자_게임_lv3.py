# 23.05.07

def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in A:
        for j in B:
            if j > i:
                B.remove(j)
                answer += 1
                break
            break
    return answer