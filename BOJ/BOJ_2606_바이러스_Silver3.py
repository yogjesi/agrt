# 2022.08.17.
# dfs

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7


N = int(input())
M = int(input())

network = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    network[i][j] = 1
    network[j][i] = 1

def dfs(network, s, visited):
    visited[s] =1
    for idx in range(1, N+1):
        if network[s][idx] == 1:
            if visited[idx] == 0:
                dfs(network, idx, visited)



visited = [0]*(N+1)

dfs(network, 1, visited)
# print(visited)
print(sum(visited)-1)