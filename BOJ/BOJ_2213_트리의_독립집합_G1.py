#...일단 dfs일 것 같긴 하다.

# N = int(input())
# weight = [] + list(map(int, input().split()))
# node = list([] for _ in range(N+1))
#
# for _ in range(N-1):
#     s, e = map(int, input().split())
#     node[s].append(e)
#     node[e].append(s)
#
#
# visited = [False]*(N+1)
#
# def dfs(node):
#     visited[node] = True
#
#
#     return

N = int(input())
tree = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
path = [[[] for _ in range(2)] for _ in range(N+1)]
W = [0] + list(map(int, input().split()))
visit = [False] * (N+1)

for _ in range(N-1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)


def dfs(node):
    visit[node] = True
    dp[node][1] += W[node]
    path[node][1].append(node)

    for x in tree[node]:
        if not visit[x]:
            result = dfs(x)
            dp[node][0] += max(dp[x][0], dp[x][1])
            dp[node][1] += dp[x][0]

            path[node][1] += result[0]
            if dp[x][0] > dp[x][1]:
                path[node][0] += result[0]
            else:
                path[node][0] += result[1]

    return path[node]


p = dfs(1)
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    p[0].sort()
    for i in p[0]:
        print(i, end=' ')
else:
    print(dp[1][1])
    p[1].sort()
    for i in p[1]:
        print(i, end=' ')