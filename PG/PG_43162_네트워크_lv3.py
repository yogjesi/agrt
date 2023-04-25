# Programmers
# 네트워크


def onenet(n, arr, idx, visited):
    visited[idx] = 1
    for cnt in range(n):  # 아 여긴 변수명 또 왜이래 헷갈리는군
        if idx != cnt and arr[idx][cnt] == 1:  # 같은 컴퓨터가 아니고 연결되어 있으면
            if visited[cnt] == 0:  # 심지어 방문한 적도 없으면
                onenet(n, arr, cnt, visited)  # 다음 걸로!


def solution(n, computers):
    answer = 0  # network 개수
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            onenet(n, computers, i, visited)  # onenet 돌고 나오면 visited가 채워질 거임
            answer += 1  # 한 루프 다 돌면 answer += 1
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])