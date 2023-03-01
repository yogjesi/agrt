# 22.08.29
# 삼성 역량 테스트 기출

# 6 2 10
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 6 4
# 5 6 3 6
# 6 1 4 1

from collections import deque

# 기본 세팅
N, M, gas = map(int, input().split())

city = []
for _ in range(N):
    city.append(list(map(int, input().split())))

drx, dry = map(int, input().split())
drx -= 1
dry -= 1

info = []
goal = []
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    info.append((sx-1, sy-1))
    goal.append((ex-1, ey-1))

print(info)
print(goal)

# bfs 선택 : 가장 가까운 손님 찾기
# 검색 순서 : 상, 좌, 우, 하 : 아 근데 이거 아니래... 아놔....
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 택시기사 위치 좌표 넣어주기 >> 손님 찾으러 간다
passenger = []
def bfs(x, y):
    fuel = 0   # 소비한 연료
    q = deque()
    q.append((x, y, fuel))
    visited = list([0]*N for _ in range(N))
    while q:
        x, y, f = q.popleft()
        visited[x][y] = 1
        if (x, y) in info:
            passenger.append((f, x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nf = f + 1   # 거리 1만큼 늘어나니까 연료 1만큼 더 소비함
            if nx < 0 or nx >= N or ny < 0 or ny >= N:   # 맵 벗어날 때
                continue
            if city[nx][ny] == 1: # 벽을 만났을 때
                continue
            if visited[nx][ny] == 1:
                continue
            # if (nx, ny) in info:
            #     passenger.append((nf, nx, ny))
                # print(passenger)
            if city[nx][ny] == 0:  # 길이 있으면
                q.append((nx, ny, nf))
                visited[nx][ny] = 1
    passenger.sort()
    # print(passenger)
    f, x, y = passenger[0]
    return x, y, f      # 이부분 고쳐줘야 하는데....


# 가능한가? 가능하다면 도착지와 소비한 연료량을 return할 것 >> 목적지 찾으러 가는 과정
def isAble(x, y, fuel):
    num = len(info)
    for idx in range(num):
        if (x, y) == info[idx]:
            ex, ey = goal[idx]
            # 태운 손님 정보는 날려주기
            info.pop(idx)
            goal.pop(idx)
            break
    dist = 0
    now = deque()
    now.append((x, y, dist))
    visited = list([0]*N for _ in range(N))
    while now:
        # print('now', now)
        x, y, d = now.popleft()
        visited[x][y] = 1
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            md = d + 1
            if mx < 0 or mx >= N or my < 0 or my >= N:   # 맵 벗어날 때
                continue
            if city[mx][my] == 1: # 벽을 만났을 때
                continue
            if visited[mx][my] == 1: # 방문한 곳이면
                continue
            if mx == ex and my == ey:
                return mx, my, md
            if city[mx][my] == 0:
                now.append((mx, my, md))
                visited[mx][my] = 1
        if md > fuel:
            return False
    return False

result = 0

for _ in range(M):
    # 손님 태우기
    get_person = bfs(drx, dry)
    print(get_person)
    if get_person == 0:
        result = -1
        break
    else:
        x, y, used_fuel = get_person
    # print(used_fuel)
    if used_fuel <= gas:
        gas = gas - used_fuel
        # 목적지 찾기
        answer = isAble(x, y, gas)
        # print('answer', answer)
        if answer == False:
            result = -1
            break
        else:
            drx, dry, dist = answer
            gas += dist
            # print('gas',gas)
    else:
        result = -1
        break

if result == -1:
    print(result)
else:
    print(gas)