# 23.04.03
# import copy
#
# def solution(n):
#     answer = 0
#     field = list([0] * n for _ in range(n))
#
#     def marker(visited, i, j):
#         dx = [1, 1]
#         dy = [1, -1]
#
#         for m in range(n - i):
#             visited[i+m][j] = 1
#             for k in range(2):
#                 nx, ny = i + dx[k] * m, j + dy[k] * m
#                 if 0 <= nx < n and 0 <= ny < n:
#                     visited[nx][ny] = 1
#                     # print('checker', m, k, visited)
#         return visited
#
#     def dfs(visited, i):
#         nonlocal answer
#         if i == n:
#             answer += 1
#             return
#
#         if sum(visited[i]) == n:
#             return
#
#         std = False
#
#         for j in range(n):
#             if visited[i][j] == 0:
#                 std = True
#                 inst = [[0]*n for _ in range(n)]
#                 for idx in range(n):
#                     for jdx in range(n):
#                         inst[idx][jdx] = visited[idx][jdx]
#                 # inst = copy.deepcopy(visited)
#                 n_visited = marker(inst, i, j)
#                 print(i, j, n_visited)
#                 dfs(n_visited, i + 1)
#         if std == False:
#             return
#
#     dfs(field, 0)
#     print(answer)
#     return answer

def solution(n):
    answer = 0
    field = []

    def checker(field, i, j):
        for idx in range(len(field)):
            if abs(i-idx) == abs(j-field[idx]):
                return False
        return True

    def nqueen(field, i):
        nonlocal answer
        if i == n:
            answer += 1
            return

        std = False

        for j in range(n):
            if j not in field and checker(field, i, j):
                std = True
                field.append(j)
                # print(field)
                nqueen(field, i+1)
                field.pop()

        if not std:
            return
    nqueen(field, 0)
    # print(answer)
    return answer

solution(12)

