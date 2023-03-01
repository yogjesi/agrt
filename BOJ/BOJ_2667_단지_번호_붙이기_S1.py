# 22.08.27
# DFS


N = int(input())

city = []
for _ in range(N):
    city.append(list(map(int, input())))

print(city)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    if visited[x][y] == 0:
        return
    return


visited = [[0]*N for _ in range(N)]
print(visited)

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            bfs(i, j, visited)