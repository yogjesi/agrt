# 23.05.15
# 문제 이름 왤케 기냐

# 맛없는 조합은 피하고 싶은 윤정이
# 선택하는 방법 몇 가지?
# 제한 : 아이스크림 종류는 200가지 이하
# 섞어먹으면 안 되는 조합 개수는 10,000가지 이하
from itertools import combinations

N, M = map(int, input().split())
bad = [[] for _ in range(N+1)]   # 0번은 비어있는 걸로
for _ in range(M):
    a, b = map(int, input().split())
    bad[a].append(b)
    bad[b].append(a)
print(bad)
kinds = [i for i in range(1, N+1)]
print('kinds', kinds)
combi = list(combinations(kinds,3))
print('combi', combi)
answer = 0
for box in combi:
    a, b, c = box
    std = True
    if b in bad[a] or c in bad[a] or c in bad[b]:
        std = False
    if std:
        answer += 1
print(answer)


# from itertools import combinations
#
# N, M = map(int, input().split())
#
# bad = []
# for _ in range(M):
#     a, b = map(int, input().split())
#     bad.append((a, b))
# icecreams = [i for i in range(1, N+1)]
# combi = list(combinations(icecreams, 3))
# new = []
# for pint in combi:
#     std = True
#     for a, b in bad:
#         if a in pint and b in pint:
#             std = False
#             break
#     if std == True:
#         new.append(pint)
#
# print(len(new))