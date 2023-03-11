# 23.03.07
from collections import deque

def solution(maps):
    answer = -1
    road = []
    h = len(maps)
    w = len(maps[0])
    s, l, e = 0, 0, 0
    for m in range(len(maps)):
        inst = []
        inst.extend(maps[m])
        road.append(inst)
        for n in range(len(inst)):
            if inst[n] == "S":
                s = (m, n)
            if inst[n] == "L":
                l = (m, n)
            if inst[n] == "E":
                e = (m, n)

    # s에서 시작해서 l에 들린 다음 e로 가기
    def bfs(x, y, c):
        q = deque()
        q.append((x, y))

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        visited = list([0]*w for _ in range(h))

        while q:
            nx, ny = q.popleft()
            for i in range(4):
                tx, ty = nx + dx[i], ny + dy[i]
                if (tx < h and ty < w and tx >= 0 and ty >= 0) and road[tx][ty] == c:
                    return visited[nx][ny] + 1
                elif (tx < h and ty < w and tx >= 0 and ty >= 0) and road[tx][ty] != "X":
                    if visited[tx][ty] != 0 and visited[tx][ty] <= visited[nx][ny] + 1:
                            q.append((tx, ty))
                    else:
                        visited[tx][ty] = visited[nx][ny] + 1
                        q.append((tx, ty))
                # print(visited)

    x, y = s
    i, j = l
    first = bfs(x, y, "L")
    # print("first", first)
    second = bfs(i, j, "E")
    # print("second", second)

    if first and second:
        answer = first + second
    else:
        answer = -1
    # print(answer)
    return answer

solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])
solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])
