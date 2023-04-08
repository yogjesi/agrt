# 23.04.08
# DFS, BFS

def solution(tickets):
    answer = []
    return answer



# 예전에 풀던 코드
# from collections import deque
# from heapq import heapify
#
#
# def solution(tickets):
#     answer = []
#
#     heapify(tickets)
#
#     def dfs(s):
#         q = []
#         q.append(s)
#         cnt = 0
#         while tickets:
#             if tickets[cnt][0] == q[-1]:
#                 e = tickets[cnt][1]
#                 q.append(e)
#                 del tickets[tickets.index([s, e])]
#                 s = e
#                 cnt = 0
#             else:
#                 cnt += 1
#         return q
#
#     answer = dfs('ICN')
#     return answer