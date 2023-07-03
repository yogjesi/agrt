# 23.07.01
# 무기공학

N, M = map(int, input().split())
wood = []
for _ in range(N):
    wood.append(list(map(int, input().split())))
kinds = [(0, -1, 1, 0), (0, -1, -1, 0), (-1, 0, 0, 1), (1, 0, 0, 1)]
answer = 0
visited = []
def boomerang(i, j, cnt):
    global answer

    if j == M:
        i, j = i+1, 0  # i를 다음 행으로 넘겨주는 코드
    ni, nj = i, j + 1  # 아래 for 문의 영향을 받지 않으면서 열을 따라 가게 만드는 코드

    if i == N:    # 끝행까지 다 체크했다는 거
        answer = max(answer, cnt)
        return

    if (i, j) not in visited:
        for k in range(4):
            a, b, c, d, = kinds[k]
            if 0 <= i+a < N and 0 <= j+b < M and 0 <= i+c < N and 0 <= j+d < M: # 범위 안 벗어나면 다음 확인
                if (i+a, j+b) not in visited and (i+c, j+d) not in visited: # visited에 없으면
                    visited.append((i, j))
                    visited.append((i+a, j+b))
                    visited.append((i+c, j+d))
                    boomerang(ni, nj, cnt + wood[i][j]*2 + wood[i+a][j+b] + wood[i+c][j+d])
                    visited.remove((i, j))
                    visited.remove((i+a, j+b))
                    visited.remove((i+c, j+d))
    boomerang(ni, nj, cnt)

boomerang(0, 0, 0)
print(answer)