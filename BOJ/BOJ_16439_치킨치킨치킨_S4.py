# 23.05.22
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
nums = [i for i in range(M)]
picks = list(combinations(nums, 3))
answer = 0
for a, b, c in picks:
    temp = 0
    for i in range(N):
        temp += max(arr[i][a], arr[i][b], arr[i][c])
    if temp > answer:
        answer = temp
print(answer)
