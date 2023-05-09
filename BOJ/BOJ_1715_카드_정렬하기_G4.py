# 23.05.09
# 카드 정렬하기
from heapq import heappush, heappop, heapify

N = int(input())
stacks = [int(input()) for _ in range(N)]
heapify(stacks)
cnt = 0
while len(stacks) > 1:
    A = heappop(stacks)
    B = heappop(stacks)
    cnt += (A+B)
    heappush(stacks, A+B)
print(cnt)

