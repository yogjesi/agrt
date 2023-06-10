# 23.06.08

from itertools import combinations

max_num = float('inf')  # 최댓값

# 1. 입력
N, M = map(int, input().split())
village = []
for _ in range(N):
    village.append(list(map(int, input().split())))

# 2. 치킨집, 가정집 좌표 찾기
restaurants = []        # 치킨집 리스트 : 2
houses = []             # 가정집 리스트 : 1
for i in range(N):
    for j in range(N):
        if village[i][j] == 2:
            restaurants.append((i, j))
        if village[i][j] == 1:
            houses.append((i, j))

# 3. 조합해서 최소 거리 구하기
combis = list(combinations(restaurants, M))     # 치킨집 M개 선택할 때의 조합
answer = max_num                                # 최솟값을 찾는 문제이므로 최댓값으로 초기화
for combi in combis:                            # 치킨집 조합을 돌면서
    dist = [max_num] * len(houses)              # dist : 집에서 치킨집까지의 최소거리 기록용
    for r, c in combi:                          # 치킨집 별 각 집과의 거리를 계산한다.
        for i, house in enumerate(houses):
            x, y = house
            d = abs(r-x) + abs(c-y)
            if d < dist[i]:
                dist[i] = d                     # 각 집 기준은 인덱스임!
    if sum(dist) < answer:                      # 거리의 합과 answer를 비교해서 answer 갱신
        answer = sum(dist)

# 4. 출력
print(answer)