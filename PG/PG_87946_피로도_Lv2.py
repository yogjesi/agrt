# 22.08.25
# 분류 : 완전 탐색
# 이진 탐색이려나?
# def dfs(graph, s, visited):
#     return
#
# def solution(k, dungeons):
#     answer = -1
#     stack = []
#     for idx in range(len(dungeons)):
#         stack.append(idx)
#         for jdx in range(len(dungeons)):
#             if jdx not in stack:
#                 dfs(dungeons, jdx, stack)
#     return answer

# 23.02.14
# 순열로 풀었음 (나자신 좀 성장했니????)
# from itertools import permutations
#
# def solution(k, dungeons):
#     answer = -1
#     for p in permutations(dungeons, len(dungeons)):
#         # print(p)
#         # 초기 값 k 를 start에 담아주기
#         start = k
#         cnt = 0
#
#         for need, use in p:
#             # print(need, use)
#             if start < need:
#                 break
#             start -= use
#             cnt += 1
#         if answer < cnt:
#             answer = cnt
#
#     return answer

# 23.02.14
# 아래는 다른 방식으로도 한 번 풀어보려고. dfs, bfs로 풀어보기
from collections import deque
def dfs():
    q = deque()
    q.append()
    visited = []

    return

def solution(k, dungeons):
    answer = -1
    return answer