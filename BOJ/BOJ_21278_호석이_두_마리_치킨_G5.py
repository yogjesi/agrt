# 23.06.08
# 완탐
from itertools import combinations
from collections import defaultdict

max_num = float('inf')
# 1. input
N, M = map(int, input().split())
info = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    info[a-1].append(b-1)
    info[b-1].append(a-1)

print(info)
# 2. find distance and record it in 'dist'

def depth(now, target, cnt, check):
    if now == target:
        return check[now]
    for num in info[now]:
        if check[num] > cnt:
            check[num] = cnt
        depth(num, target, cnt+1, check)


candidates = list(combinations(range(N), 2))
print(candidates)
inst = [0]*N
for a, b in candidates:
    for i in range(N):
        if i in [a, b]:
            inst[i] = 0
        if a in info[i] or b in info[i]:
            inst[i] = 1
        else:
