# 23.04.25
# dfs의 함정에 빠지지 말자...
# 누적의 개념을 잘 떠올리자...
def solution(land):
    field = [[0] * 4 for _ in range(len(land))]
    # print(field)

    field[0] = land[0]
    # print(field)
    for r in range(1, len(land)):
        for c in range(4):
            c1, c2, c3 = [n for n in range(4) if n != c]
            field[r][c] = land[r][c] + max(field[r - 1][c1], field[r - 1][c2], field[r - 1][c3])
    # print(field)
    answer = max(field[-1])

    return answer

# def solution(land):
#     answer = 0
#
#     def dfs(n, cnt, pre):
#         nonlocal answer
#         if n == len(land):
#             if answer < cnt:
#                 answer = cnt
#                 # print(answer)
#             return
#         for i in range(4):
#             if pre == i:
#                 continue
#             inst = land[n][i]
#             dfs(n + 1, cnt + inst, i)
#     dfs(0, 0, -1)
#     return answer