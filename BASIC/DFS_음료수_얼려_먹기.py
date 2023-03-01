# 22.08.26.
# BFS, DFS

# 4 5
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0


N, M = map(int, input().split())

ice_grid = []
for _ in range(N):
    ice_grid.append(list(map(int, input().split())))

print(ice_grid)

def dfs(x, y):
    # ice_grid를 벗어나면 바로 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if ice_grid[x][y] == 0:  # 0이면 물을 채울 수 있는 공간이니까...
        ice_grid[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)