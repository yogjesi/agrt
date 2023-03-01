# 22.08.27
# bfs

# 0 : 안익음
# 1 : 익음
# -1 : 빈칸
# 반환값: 다 익는 일수, 만약 다 익어있다면 0, 다 익을 수 없다면 -1 반환
from collections import deque

M, N = map(int, input().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))

# print(box)

dx = [-1, 1, 0, 0 ]
dy = [0, 0, -1, 1]

q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if box[nx][ny] != 0:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))

    # print(box)

    maxinum = -2
    for k in range(N):
        if box[k].count(0) > 0:
            return -1
        inst_num = max(box[k])
        if inst_num > maxinum:
            maxinum = inst_num

    return maxinum-1

result = bfs()
print(result)