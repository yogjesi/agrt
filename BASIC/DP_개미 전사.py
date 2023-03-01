# 220쪽


N = int(input())
stock = list(map(int, input().split()))

d = [0] * 100

d[0] = stock[0]
d[1] = max(stock[0], stock[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+stock[i])

print(d[N-1])