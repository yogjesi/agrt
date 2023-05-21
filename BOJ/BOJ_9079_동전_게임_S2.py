# 23.05.20
# 동전 게임
# 제한시간 1초
from collections import deque
# 입력부
T = int(input())

for tc in range(1, T+1):
    answer = -1
    board = [list(input().split()) for _ in range(3)]
    print(board)

    # 아무 아이디어도 떠오르지 않으면 어떻게 하나요...
