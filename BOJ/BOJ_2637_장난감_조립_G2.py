#
# N = int(input())
# M = int(input())
# parts = list([0]*(N+1) for _ in range(N+1))
# for _ in range(M):
#     x, y, z = map(int, input().split())
#     parts[x][y] = z
# # print(parts)
# solid = {}
# standard = []
# for idx in range(1, N+1):
#     if sum(parts[idx]) == 0:
#         solid[idx] = 0
#         standard.append(idx)
#     else:
#         break
# # print(solid)
#
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if j not in standard:
#             multi = parts[i][j]
#             for k in range(1, N+1):
#                 parts[i][k] = parts[j][k]*multi + parts[i][k]
#             parts[i][j] = 0
# # print(parts)
#
# for m in range(N+1):
#     if parts[N][m] != 0:
#         print('{} {}'.format(m, parts[N][m]))



################################################



from collections import deque

n = int(input())


# connect : 중간부품 기록용, needs : 기본 부품
connect = [[] for _ in range(n + 1)]
needs = [[0] * (n + 1) for _ in range(n + 1)]

q = deque()

# degree(차수) :  각 넘버에 해당하는 것들이 몇 개 필요한지
degree = [0] * (n + 1)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    connect[b].append((a, c))    # a를 만들려면 b가 c개가 있어야 한다.
    degree[a] += 1


for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
print(q)
print(connect)
# q에는 표준 부품만 들어있음 --> 표준 부품에 연결된 거 몇 개인지 세어가지고... 여튼 세준다는 느낌.
while q:
    now = q.popleft()

    for next, next_need in connect[now]:   # connect에는 now번째 부품으로 만들 수 있는 부품(=next)과 필요한 now의 개수(=next_need)가 들어가있다.
        if needs[now].count(0) == n + 1:   # needs가 완전 비어있을 때(전부 0으로 되어있을 때,
            needs[next][now] += next_need
        else:
            for i in range(1, n + 1):      # needs가 비어있지 않을 때(즉 중간 부품일 때) : 기본 부품 여러개로 되어있을 거니까
                needs[next][i] += needs[now][i] * next_need

        degree[next] -= 1
        print(needs)
        if degree[next] == 0:
            q.append(next)

# 있는 것만 출력
for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)

