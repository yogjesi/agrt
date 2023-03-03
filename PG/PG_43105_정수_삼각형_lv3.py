# 23.03.03


def solution(triangle):
    answer = 0
    depth = len(triangle)
    visited = []
    for i in range(1,depth+1):
        inst = [0]*i
        visited.append(inst)
    visited[depth-1][::] = triangle[depth-1][::]
    # print(visited)

    for i in range(depth, 0, -1):
        for j in range(i-1):
            num = max(visited[i-1][j], visited[i-1][j+1])
            visited[i-2][j] = triangle[i-2][j] + num
    # print(visited)

    return visited[0][0]


result = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
print(result)