# 22.08.22

# 둘째 줄부터 N개의 줄에 공간의 상태가 주어진다.
# 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.
# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치

from collections import deque
INF = 1e9

N = int(input())

sea = []
for i in range(N):
    sea.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0, 0

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            now_x, now_y = i, j
            sea[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS일 것 같지...?
# 짧은 거리
# 고려사항 : 작은 거나 같은 건 지나갈 수 있음!!!!
def shortest():
    dist = [[-1]*N for _ in range(N)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx and nx<N and 0<=ny and ny<N:
                if dist[nx][ny] == -1 and sea[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

# 먹을 거
def eat(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(N):
        for j in range(N):
            if dist[i][j] != -1 and 1 <= sea[i][j] and sea[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0

while True:
    value = eat(shortest())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        sea[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0
