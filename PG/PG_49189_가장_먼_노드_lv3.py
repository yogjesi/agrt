# 실패한 코드 1
# def solution(n, edge):
#     edge.sort()
#     data = [0] * (n + 1)
#     data[1] = 1
#     # print(edge)
#     for node in edge:
#         [s, e] = node
#         if data[e] > data[s] + 1 and data[s] != 0:
#             data[e] = data[s] + 1
#         elif data[e] == 0 and data[s] != 0:
#             data[e] = data[s] + 1
#         elif data[s] > data[e] + 1 and data[e] != 0:
#             data[s] = data[e] + 1
#         elif data[s] == 0 and data[e] != 0:
#             data[s] = data[e] + 1
#     # print(data)
#
#     farthest = max(data)
#     answer = data.count(farthest)
#     return answer


from collections import deque


def solution(n, edge):
    edge.sort()
    visited = [0] * (n + 1)
    visited[1] = 1
    data = list([] for _ in range(n + 1))
    for node in edge:
        s, e = node
        data[s].append(e)
        data[e].append(s)

    print(data)

    q = deque()
    q.append(1)
    while q:
        s = q.popleft()
        for e in data[s]:
            if not visited[e]:
                visited[e] = visited[s] + 1
                q.append(e)

    farthest = max(visited)
    answer = visited.count(farthest)
    if answer <= 0:
        answer = 1

    return answer