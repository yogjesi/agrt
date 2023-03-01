# 2022.10.17


# 이동가능한 방향 찾고
# 이동하고 저장
# 5회 되면 종료
# 근데 이걸 완전탐색 해야 하나? 그렇겠지?ㅠㅠ

# # 1. 이동가능한 방향 찾기

from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer, q = 0, deque()


def get(i, j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j] = 0

def merge(i, j, di, dj):
    while q:
        x = q.popleft()
        if not board[i][j]: # 0이면 가만히 놔둠
            board[i][j] = x
        elif board[i][j] == x: #같은 값이라면
            board[i][j] = x*2
            i, j = i + di, j + dj
        else: # 다른 거면, 이동해야 하는 거면 이동만 시키면 됨!
            i, j = i + di, j + dj
            board[i][j] = x


# 움직이는 건 네 방향이 있음.
# k값이 0, 1, 2, 3일 때 각각 상, 하, 좌, 우로 움직임
def move(k):
    if k == 0:
        for j in range(n):
            for i in range(n):
                get(i, j)  # 보드의 (i, j)에 해당되는 자리의 숫자 q에 집어넣자
            merge(0, j, 1, 0)
    elif k == 1:
        for j in range(n):
            for i in range(n-1, -1, -1):
                get(i, j)
            merge(n-1, j, -1, 0)
    elif k == 2:
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1)
    else:
        for i in range(n):
            for j in range(n-1, -1, -1):
                get(i, j)
            merge(i, n-1, 0, -1)

def solve(count):
    global board, answer
    if count == 5:
        for i in range(n):
            answer = max(answer, max(board[i]))
        return
    b = [x[:] for x in board]

    for k in range(4): #4방향
        move(k)
        solve(count + 1)
        board = [x[:] for x in b]

solve(0)
print(answer)