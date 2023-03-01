import heapq

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(land, height):
    n = len(land)
    visited = [[False]*n for _ in range(n)]
    heap = [[0, 0, 0]]
    answer = 0

    while heap:
        v, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        answer += v
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if abs(land[x][y] - land[nx][ny]) > height:
                    heapq.heappush(heap, [abs(land[x][y] - land[nx][ny]), nx, ny])
                else:
                    heapq.heappush(heap, [0, nx, ny])
    return answer
