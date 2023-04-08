from collections import defaultdict

n, m, k = map(int, input().split())

# 1. 필드 설정
field = []
for _ in range(n):
    field.append(list(map(int, input().split())))

# 1-2. 혹시 모르는 총...용....근데 이거 아닌거 같음.
guns = defaultdict(list)
for i in range(n):
    for j in range(n):
        num = str(i) + str(j)
        guns[num] = []

players = []
infos = []
for _ in range(m):
    x, y, d, s = map(int, input().split())
    players.append((x - 1, y - 1))
    infos.append((d, s, 0))
# print(players)

# 3. 점수 관리
score = [0] * m

# 4. 움직일 때 필요한 상, 우, 하, 좌 순의 방향 설정
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


# 5. 범위 확인용 코드
def in_range(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False


# 6. 총 정렬 : 항상 제일 큰 게 필드에 나올 거임
# 여기서 i는 guns 딕셔너리 찾는 자리숫자임.
def arange_gun(x, y, i):
    if guns[i]:
        now = field[x][y]
        every_g = []
        every_g.append(now)
        every_g.extend(guns[i])
        most = max(every_g)
        if now == most:
            pass
        else:
            guns[i].remove(most)
            guns[i].append(now)
            field[x][y] = most


# 7. 진 팀 이동 (진 팀의 자리 및 기타 정보 넣기)
def lose(player, info, idx):
    # 7-1. 정보 풀어주고
    xx, yy = player
    dd, ss, gg = info
    # print(idx, '번 플레이어, 져서 빈 자리 찾는 중')
    nn = str(xx) + str(yy)
    # 7-2. 총을 정리한다.
    if field[xx][yy] > 0:  # 자리에 총이 있는 경우
        arange_gun(xx, yy, nn)  # 총 정리 해주고
        if field[xx][yy] > gg:
            guns[nn].append(gg)
        else:
            guns[nn].append(field[xx][yy])
            field[xx][yy] = gg

    # 7-3. 이제 움직여야 함
    nx, ny = xx + dxs[dd], yy + dys[dd]  # 움직이자
    # 7-3-1. 격자 안 벗어나고 플레이어도 없으면 그대로 감
    if in_range(nx, ny) and (nx, ny) not in players:
        players[idx] = (nx, ny)
        if field[nx][ny] > 0:
            gg, field[nx][ny] = field[nx][ny], gg
            infos[idx] = (dd, ss, gg)
            nn = str(nx) + str(ny)
            arange_gun(nx, ny, nn)
            # print(idx,'번 플레이어 자리', (nx, ny))
    # 7-3-2. 범위를 벗어나거나 다른 플레이어가 있으면 오른쪽으로 90도씩 회전하다 빈칸이 보이는 순간 바로 이동.
    else:
        for rr in range(4):
            dd += 1
            if dd > 3:
                dd = dd % 4
            nx, ny = xx + dxs[dd], yy + dys[dd]  # 새로운 방향으로 갱신
            if in_range(nx, ny) and (nx, ny) not in players:
                players[idx] = (nx, ny)
                # 만약 해당 칸에 총이 있다면 가장 공격력이 높은 총을 획득
                if field[nx][ny] > 0:
                    infos[idx] = (dd, ss, field[nx][ny])
                    field[nx][ny] = 0
                    nn = str(nx) + str(ny)
                    arange_gun(nx, ny, nn)
                else:
                    infos[idx] = (dd, ss, 0)
                # print(idx, '번 플레이어 자리', (nx, ny))
                break

# 8. 이긴 팀
# 2-2-3. 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득
# 나머지 총은 해당 격자에 내려놓음
def win(player, info, idx):
    xx, yy = player
    dd, ss, gg = info
    if field[xx][yy] > gg:
        infos[idx] = (dd, ss, field[xx][yy])
        field[xx][yy] = gg
        nn = str(xx) + str(yy)
        arange_gun(xx, yy, nn)


def simulate():
    # 1. 본인이 향한 방향대로 한 칸 만큼 이동
    # 만일 격자를 벗어나는 경우, 정반대 방향으로 바꾸어서 1만큼 이동
    for i in range(m):
        # print(i, '번 player')
        x, y = players[i]
        d, s, g = infos[i]
        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny):
            if d == 0:
                d = 2
            elif d == 1:
                d = 3
            elif d == 2:
                d = 0
            else:
                d = 1
            nx, ny = x + dxs[d], y + dys[d]
        # print('step1', players[i], infos[i])
        infos[i] = (d, s, g)

        # 2-1. 이동한 방향에 플레이어가 없는 경우
        # 해당 칸에 총이 있는지 확인, 더 센 총을 획득
        if (nx, ny) not in players:
            if field[nx][ny] > g:
                g, field[nx][ny] = field[nx][ny], g
                infos[i] = (d, s, g)
                num = str(nx) + str(ny)
                arange_gun(nx, ny, num)
            # 위치 갱신
            players[i] = (nx, ny)

        # 2-2. 이동한 방향에 플레이어가 있는 경우
        # 종합 점수 = 플레이어의 초기 능력치 + 총의 공격력
        # 각 플레이어의 종합 점수를 비교, 만약 같다면 플레이어의 '초기 능력치'가 높은 플레이어가 승리함
        # 이긴 플레이어는 총 수치 차이만큼을 포인트로 획득
        else:
            j = players.index((nx, ny))
            # 기존 자리에 있던 플레이어의 정보(j번 플레이어)
            jd, js, jg = infos[j]
            ip, jp = s + g, js + jg
            players[i] = (nx, ny)
            # 종합 점수가 다르다면 누가 승리했는지 바로 가리자
            if ip != jp:
                if ip > jp:  # j가 졌음
                    score[i] = ip - jp
                    lose(players[j], infos[j], j)
                    win(players[i], infos[i], i)
                else:  # i가 졌음
                    score[j] = jp - ip
                    lose(players[i], infos[i], i)
                    win(players[j], infos[j], j)

            # 수치가 같다면 플레이어 초기 능력치 비교, score는 0점이겠지 뭐...
            else:
                if s > js:  # i가 이긴 경우
                    lose(players[j], infos[j], j)
                    win(players[i], infos[i], i)

                else:  # j가 이긴 경우
                    lose(players[i], infos[i], i)
                    win(players[j], infos[j], j)
        # print('step2', players[i], infos[i])
    # print(score)


# 최종 : k라운드 만큼 돌림
for r in range(k):
    # print(r, 'round')
    simulate()

for ans in score:
    print(ans, end=" ")
