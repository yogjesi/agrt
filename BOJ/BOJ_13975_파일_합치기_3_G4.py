# 23.05.02

# 아이디어 : 1.작은 것 찾아서 2.더하고 3.넣기 4.반복
from heapq import heapify, heappush, heappop

T = int(input())

for tc in range(1, T+1):
    K = int(input())
    cts = list(map(int, input().split()))
    heapify(cts)
    answer = 0
    # 4. 반복
    while len(cts) > 1:
        # 1. 작은 것 두 개 찾기
        a = heappop(cts)
        b = heappop(cts)
        # 2. 더하기
        num = a + b
        answer += num
        # 3. 넣기
        heappush(cts, num)
    print(answer)