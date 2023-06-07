# 23.06.08
# 첫 번 째 : 통과 / 하지만 시간을 줄이고 싶다 / 줄일 수 있을 거 같은데.. 흑흑...

from itertools import combinations

# 1. 입력
N, M = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

answer = 0                                  # 정답 초기화
# 2. tetromino 찾는 함수 작성
def tetromino(now, cnt, i, j, visited):
    global answer                           # global로 answer에 접근
    if now == 4:                            # 2-1. 베이스 조건 : 네 개의 정사각형을 모두 붙였다면
        if cnt > answer:                    # answer 변경 여부 확인
            answer = cnt                    # answer 변경
        return

    # 방향 조작용
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
                                                    # 2-2. 하나를 중심으로 둘러싸인 특이 케이스 (dfs로 접근 불가)
    if now == 0:                                    # visited에 하나만 있을 때 옆을 둘러싼 세 개를 한 꺼번에 계산할 것임
        nums = [] # 후보 받을 곳
        for n in range(4):
            dx, dy = i + dxs[n], j + dys[n]
            if 0 <= dx < N and 0 <= dy < M:         # 범위를 벗어나지 않으면 일단 후보에 넣음
                nums.append((dx, dy))
        able = list(combinations(nums, 3))          # 조합을 이용해 옆을 둘러쌀 수 있는 경우의 수 구함
        # print(able)
        if able:                                    # 만일 경우의 수들이 존재한다면 계산해서 answer 업데이트 하기
            for (a, b), (c, d), (e, f) in able:
                subtotal = cnt + field[a][b] + field[c][d] + field[e][f]
                if subtotal > answer:
                    answer = subtotal

    for n in range(4):                                                  # 2-3. dfs
        nx, ny = i + dxs[n], j + dys[n]
        if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:     # 범위를 벗어나지 않고 방문한 적 없다면
            visited.append((nx, ny))                                    # 방문 처리하고
            tetromino(now+1, cnt+field[nx][ny], nx, ny, visited)        # 다음 tetromino 수행
            visited.remove((nx, ny))                                    # 방문 체크 해제

# 3. 동작 : field의 모든 칸을 돌면서 tetromino 수행
for i in range(N):
    for j in range(M):
        visited = [(i, j)]  # 일단 초기값 넣고 시작
        tetromino(1, field[i][j], i, j, visited)

# 4. 출력
print(answer)