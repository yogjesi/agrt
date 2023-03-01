# Programmers
# 네트워크


def solution(n, computers):
    network = 0 # network 개수
    visited = [0]*n # 들린 곳
    for i in range(n):
        if visited[i] == 0:
            onenet(n, computers, i, visited)
            network += 1 # 다 돌아서 네트워크 하나 완성하면 +1 올려주기
    # print(network)
    return network


def onenet(n, arr, idx, visited):
    visited[idx] = 1
    for cnt in range(n):
        if idx!=cnt and arr[idx][cnt]==1:
            if visited[cnt]==0:
                onenet(n, arr, cnt, visited)

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])