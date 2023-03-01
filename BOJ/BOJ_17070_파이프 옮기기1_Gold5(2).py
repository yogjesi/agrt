from collections import deque
import sys

input = sys.stdin.readline

# 입력
N = int(input())
home = []
for _ in range(N):
    home.append(list(map(int, input().split())))


def dfs(er, ec, state):
    global cnt
    if er == N-1 and ec == N-1:
        cnt += 1
        return
    if state == 0 or state == 1 or state == 2:  # 대각선으로 갈 수 있는 녀석들
        if er + 1 < N and ec + 1 < N and home[er+1][ec] == 0 and home [er][ec+1] == 0 and home [er+1][ec+1] == 0:
            dfs(er + 1, ec + 1, 2)
    if state == 0 or state == 2:   # 오른쪽으로 갈 수 있는 녀석들
        if ec + 1 < N and home[er][ec+1] == 0:
            dfs(er, ec+1, 0)
    if state == 1 or state == 2:
        if er + 1 < N and home[er+1][ec] == 0:
            dfs(er+1, ec, 1)

cnt = 0

# 가로, 세로, 대각선 = 0, 1, 2
dfs(0, 1, 0)

print(cnt)