from collections import deque


def solution(people, limit):
    q = deque()
    people.sort()
    q.extend(people)
    print(q)

    answer = 0
    while q:
        extra = limit - q[-1]
        q.pop()
        cnt = 0
        while extra >= 0 and cnt < len(q):
            if q[cnt] > extra:
                break
            elif q[cnt] <= extra:
                extra -= q[cnt]
                q.popleft()
            else:
                cnt += 1
        answer += 1
    return answer