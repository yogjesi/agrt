from collections import deque
import sys


input = sys.stdin.readline
# 1시간 9분


# 입력
N = int(input())
home = []
for _ in range(N):
    home.append(list(map(int, input().split())))

# 표시
result = list([0]*N for _ in range(N))

# 파이프 배치 형태(가로/세로/대각선) 파악해서 각각에 맞는 미는 법 코드
def pipe_status(pipe):
    sr, sc, er, ec = pipe
    if sr == er:   # 행이 같을 때
        if ec + 1 < N and er + 1 < N and home[er][ec+1] == 0 and home[er+1][ec] == 0 and home[er+1][ec+1] == 0:
                num = 2
                way = [(0, 1, 0, 1), (0, 1, 1, 1)]
        elif ec + 1 < N and home[er][ec+1] == 0:
            num = 1
            way = [(0, 1, 0, 1)]
        else:
            return 0, [(0, 0, 0, 0)]
    elif sc == ec:   # 열이 같을 때
        if er + 1 < N and ec + 1 < N and home[er+1][ec] == 0 and home[er][ec+1] == 0 and home[er+1][ec+1] == 0:
            num = 2
            way = [(1, 0, 1, 0), (1, 0, 1, 1)]
        elif er + 1 < N and home[er+1][ec] == 0:
            num = 1
            way = [(1, 0, 1, 0)]
        else:
            return 0, [(0, 0, 0, 0)]
    else:   # 대각선일때
        if ec + 1 < N and er + 1 < N :
            if home[er+1][ec] == 0 and home[er][ec+1] == 0 and home[er+1][ec+1] == 0:
                num = 3
                way = [(1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]
            elif home[er+1][ec] == 0 and home[er][ec+1] == 0:
                num = 2
                way = [(1, 1, 0, 1), (1, 1, 1, 0)]
            elif home[er+1][ec] == 0:
                num = 1
                way = [(1, 1, 1, 0)]
            elif home[er][ec+1] == 0:
                num = 1
                way = [(1, 1, 0, 1)]
            else:
                return 0, [(0, 0, 0, 0)]
        elif ec + 1 < N and home[er][ec+1] == 0:
            num = 1
            way = [(1, 1, 0, 1)]
        elif er + 1 < N and home[er+1][ec] == 0:
            num = 1
            way = [(1, 1, 1, 0)]
        else:
            return 0, [(0, 0, 0, 0)]
    return num, way


# 완전탐색 돌리기 (근데 너무 많아질 것 같으니까 줄이는 방법 생각해보기)
def find_way(pipe):
    sr, sc, er, ec = pipe
    q = deque()
    q.append((sr, sc, er, ec))
    cnt = 0
    while q:
        now_pipe = q.popleft()
        nsr, nsc, ner, nec = now_pipe
        if ner == N-1 and nec == N-1:
            cnt += 1
            continue
        nums, ways = pipe_status(now_pipe)
        if nums == 0:
            continue
        # print(nums, ways)
        for i in range(nums):
            i, j, k, l = ways[i]
            new_pipe = (nsr + i, nsc + j, ner + k, nec + l)
            q.append(new_pipe)
    return cnt

# 파이프 시작 위치
pipe = (0, 0, 0, 1)

result = find_way(pipe)
print(result)