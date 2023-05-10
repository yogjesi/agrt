# 23.05.10
# 택배 : 그리디

N, C = map(int, input().split())

M = int(input())

info = []
road = [0]*(N+1)
for _ in range(M):
    s, e, box = map(int, input().split())
    info.append((s, e, box))
print(info)
info.sort()
print(info)
cnt = 0
# 빨리 떨어지는 것(=배달 간격이 좁은 것)부터 채워넣으면 되지 않을까?
for i in range(1, N+1): # 택배 이동
    while cnt < C:      # 화물 적재
