# 23.06.22
# 약 1시간 30분


# 1. 입력부
N, M, K = map(int, input().split())
# 1-1. 노트북 겉때기 만들기
plate = [[0]*M for _ in range(N)]
print(plate)

# 2. 자리 확인
# stk: 부착하려는 스티커, now: 필드에서 지정한 범위
# w: 스티커 가로, h: 스티커 세로
def isAbleToAttatch(stk, now, h, w):
    for i in range(h):
        for j in range(w):
            if stk[i][j] == 1:
                if now[i][j] != 0:
                    return False
    return True

# 3. 90도 회전 함수
def rotation(stk, h, w):
    new_stk = [[0]*h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            new_stk[j][h-1-i] = stk[i][j]
    return new_stk, len(new_stk), len(new_stk[0])

# 1-2. 스티커 차례로 하나씩 확인
for k in range(K):
    # print(k+1, "번 스티커")
    r, c = map(int, input().split())
    sticker = []
    for _ in range(r):
        sticker.append(list(map(int, input().split())))
    # 위의 과정을 거치면 새로운 스티커 하나 탄생

    # 4. plate위 부착가능성 확인 + 부착
    state = False
    for _ in range(4):
        for i in range(N-r+1):
            for j in range(M-c+1):
                inst = plate[i:i+r]
                field = []
                for x in inst:
                    field.append(x[j:j+c])
                # print("test", field)
                result = isAbleToAttatch(sticker, field, r, c)
                if result:
                    for idx in range(r):
                        for jdx in range(c):
                            if sticker[idx][jdx] == 1:
                                plate[idx + i][jdx + j] = sticker[idx][jdx]
                    state = True
                    # print("현재 노트북은", plate)
                    break
            if state:
                break
        if state:
            break
        sticker, r, c = rotation(sticker, r, c)
        # print("돌린 스티커는 : " , sticker)

# 5. 합계
answer = 0
for n in range(N):
    answer += sum(plate[n])
print(answer)
