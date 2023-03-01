from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        res = board
        row = len(board)
        col = len(board[0])
        v = [[0] * col for _ in range(row)]

        # 4방향 돌아다닐거임
        queue = deque()
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        # 가장자리 체크 : 가장자리 O는 X로 못 바꿈
        for i in range(col):
            if board[0][i] == 'O':
                queue.append([0, i])
            if board[row - 1][i] == 'O':
                queue.append([row - 1, i])
        for i in range(row):
            if board[i][0] == 'O':
                queue.append([i, 0])
            if board[i][col - 1] == 'O':
                queue.append([i, col - 1])

        # 탐색
        while queue:
            x, y = queue.popleft()
            v[x][y] = 1
            for i in range(4):
                newX, newY = x + dx[i], y + dy[i]

                if 0 <= newX and newX < row and 0 <= newY and newY < col and v[newX][newY] == 0 and board[newX][newY] == 'O':
                    v[newX][newY] = 1
                    queue.append([newX, newY])

        # 변환
        for i in range(row):
            for j in range(col):
                if v[i][j] == 0:
                    res[i][j] = 'X'
                else:
                    res[i][j] = 'O'
        return res

