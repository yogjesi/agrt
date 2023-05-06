# 23.05.06
# DFS
def dfs(x, y, w, h, visited, field):
    if (x, y) in visited:
        return
    if field[x][y] == 0:
        return
    visited.append((x, y))
    dxs = [0, 1, 0, -1, 1, 1, -1, -1]
    dys = [1, 0, -1, 0, 1, -1, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w:   # if nx, ny are in range:
            if field[nx][ny] == 1:        # if field[i][j] is land:
                dfs(nx, ny, w, h, visited, field)

while True:
    w, h = map(int, input().split())
    # Escape when w, h have 0
    if w == 0 and h == 0:
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    visited = []



