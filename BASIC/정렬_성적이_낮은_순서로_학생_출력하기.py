# 22.08.26
# 정렬

N = int(input())

l = []
for _ in range(N):
    name, score = input().split()
    l.append((int(score), name))

l.sort()
for i in range(N):
    print(l[i][1], end=' ')