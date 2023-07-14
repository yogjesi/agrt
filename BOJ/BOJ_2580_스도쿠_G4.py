# 23.07.10

# 1. 입력부
sdoku = []              # 스도쿠 판 받을 거
blanks = []             # 비어있는 칸 좌표 리스트
for i in range(9):
    temp = list(map(int, input().split()))
    sdoku.append(temp)
    for j, num in enumerate(temp):
        if num == 0:
            blanks.append((i, j))           # 비어있는 좌표 blanks에 저장하기

print(sdoku)
print(blanks)

# 값이 0인 좌표를 싹 모아놓고, queue에 넣고,
# 하나씩 뽑아서, 만일 바로 확정할 수 있으면 바로 숫자를 넣고
# 그렇지 않으면 다시 queue에 넣고 반복하면 되지 않을까?

# 체크해야 할 건 가로, 세로, 그리고 3*3 구획 내의 숫자들
def checker(x, y):
    global sdoku
    for n in range(1, 10): # horizontal
        if n not in sdoku[x] and sdoku[x].count(0) == 1:
            sdoku[x][y] = n
            return True

    num_list = [0]*10
    for m in range(9):      # vertical
        if sdoku[m][y] != 0:
            num_list[sdoku[m][y]] = 1
    if sum(num_list) == 8:
        for i in range(1, 10):
            if num_list[i] == 0:
                sdoku[x][y] = i






