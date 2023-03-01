# 96쪽

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

N, M = map(int, input().split())
answer = 0
for _ in range(N):
    row = list(map(int, input().split()))
    answer = max(answer, min(row))
print(answer)