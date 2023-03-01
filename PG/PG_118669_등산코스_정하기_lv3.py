# 2022.09.19
# 스터디

# test case
# n = 6
# paths : [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
# gates : [1, 3]
# summits : [5]

from collections import deque, defaultdict
from heapq import heappush, heappop

def solution(n, paths, gates, summits):

    # 해당 경로에서는 최대이면서 모든 경로 중에는 최소값을 가지는 intensity 찾는 함수
    def min_intensity():
        pq = []
        # 근데 priority queue도 따로 있는 것 같던데 왜 heapq를 쓰는 걸까? >>> thread_safe의 유무로 heapq가 더 빠르대!
        visited = [10000001]*(n+1)

        # 1. 출발지는 정해져있으니 담아두자.
        for gate in gates:
            heappush(pq, (0, gate))
            visited[gate] = 0

        # 2. 경로 탐색 >> 산봉우리에 도달하면 끝.
        # (그러나 뭐가 최소인지 모르므로 모든 산봉우리를 돌아볼 것임.)
        while pq:
            intensity, node = heappop(pq)

            # 봉우리에 도달하거나 / intensity가 기록된 것보다 더 크면 갈 필요가 없으니 멈추고 다른 경로 찾기
            if node in set_summits or intensity > visited[node]:
                continue

            for w, next_n in graph[node]:
                # 두 개 중 큰 값을 새로운 intensity로 잡는 과정
                new_i = max(intensity, w)
                # 위에서 새롭게 선정된 intensity가 기존에 visited에 기록된 intensity보다 더 작을 경우에만
                # 값을 바꿔주고 경로를 추가해주는 것이 의미가 있으므로
                if new_i < visited[next_n]:
                    visited[next_n] = new_i    # 값 바꿔주고
                    heappush(pq, (new_i, next_n))    # 경로에 넣어주고

        answer = [0, 10000001]
        for summit in summits:
            if visited[summit] < answer[1]:
                answer[0] = summit
                answer[1] = visited[summit]
        return answer

    summits.sort()                # 정렬해서 작은 봉우리부터 갈 수 있도록!
    set_summits = set(summits)    # 이거 아직 의문... 왜 set을 써야되지?
    graph = defaultdict(list)     # defaultdict : default 값을 list로 줘서 dictionary로 만들겠다는 거임
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    return min_intensity()


test = solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5])
print(test)