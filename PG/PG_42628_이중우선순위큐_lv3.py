# 23.03.08

from collections import deque

def solution(operations):
    answer = []
    q = deque()
    while operations:
        c, n = operations.pop(0)
        if c == "I":
            q.append(n)
        elif c == "D":
            if n == 1:   # 최댓값 삭제

                pass
            else:        # 최솟값 삭제
                pass

    print(operations)
    return answer