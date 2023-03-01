# 2022.09.22
# 2020 KAKAO BLIND RECRUITMENT

# N*N : 자물쇠
# M*M : 열쇠
# N >= M

# 일단 첫번째 아이디어 떠올리는데 무려 30분이 걸림... 후...
# 하지만 첫번째 아이디어가 맞았다!!!!!
# 약 2시간 10분 소요

import copy

def solution(key, lock):
    M = len(key)
    # original key는 그대로 두자

    # 1. rolling은 열쇠를 한 방향으로 90도 돌리는 함수
    def rolling(k):
        key_rolled = list([0]*M for _ in range(M))
        for i in range(M):
            for j in range(M):
                key_rolled[i][j] = k[j][M-1-i]     # 왼쪽으로 90도
                # key_rolled[j][M-1-i] = k[i][j]   # 오른쪽으로 90도
        return key_rolled

    # 2. 자물쇠 크기 변경 (모서리부터 차곡차곡 열쇠를 넣어볼 수 있도록)
    N = len(lock)
    new_lock = list([0]*(N+(M-1)*2) for _ in range(N+(M-1)*2))
    for i in range(N):
        for j in range(N):
            new_lock[M-1+i][M-1+j] = lock[i][j]
    # print(new_lock)

    # 4. 열쇠구멍에 맞는지?
    def isFit(arr):
        l = len(arr)
        for i in range(l):
            if arr[i].count(0) >= 1:
                return False
            if arr[i].count(1) < l:
                return False
        return True

    # 3. 열쇠와 자물쇠 체결 시도 + 아니면 원상태 복구하고 다시 옮겨서 체결
    def put_the(k):
        inst_lock = copy.deepcopy(new_lock)    # 시간? 메모리? 주의
        for a in range(M+N-1):
            for b in range(M+N-1):
                for x in range(M):
                    for y in range(M):
                        inst_lock[x+a][y+b] += k[x][y]
                center_lock = inst_lock[M-1:N+M-1]
                for num in range(len(center_lock)):
                    center_lock[num] = center_lock[num][M-1:N+M-1]
                # print(center_lock)
                if isFit(center_lock):
                    return True
                else:
                    inst_lock = copy.deepcopy(new_lock)
        return False

    for n in range(4):
        if n == 0:
            new_key = key
            print(new_key)
            answer = put_the(new_key)
            if answer == True:
                return True
        else:
            new_key = rolling(new_key)
            print(new_key)
            answer = put_the(new_key)
            if answer == True:
                return True
    return False


# result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
result = solution([[0, 0, 0], [0, 1, 0], [1, 1, 0]], [[1, 1, 1, 1],[1, 0, 0, 1],[1, 1, 0, 1], [1, 1, 1, 1]])
print(result)