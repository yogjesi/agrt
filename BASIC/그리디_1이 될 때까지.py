# 99쪽


N, K = map(int, input().split())

cnt = 0
while N >= K:
    if N%K == 0:
        N = N//K
    else:
        N -= 1
    cnt += 1

cnt += (N-1)

print(cnt)