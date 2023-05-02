# 23.05.02

N = int(input())
answer = 0

# idea : 라인 타고 내려와서 윗라인과 안 겹치게??
def checker(field, i, j):
    for idx in range(len(field)):
        if abs(i-idx) == abs(j-field[idx]):
            return False
    return True

def nqueen(field, i):
    global answer
    if i == N:
        answer += 1
        return

    std = False
    for j in range(N):
        if j not in field and checker(field, i, j):
            std = True
            field.append(j)
            nqueen(field, i+1)
            field.pop()
    if not std:
        return
field = []
nqueen(field, 0)
print(answer)