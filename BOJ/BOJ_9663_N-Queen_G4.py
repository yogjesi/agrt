# 23.05.02
# 23.07.01

# pypy만 통과
# N = int(input())
# answer = 0
# field = [0]*N
# def checker(i):
#     for j in range(i):
#         if field[i] == field[j] or abs(field[i] - field[j]) == abs(i-j):
#             return False
#     return True
#
# def nqueen(i):
#     global answer
#     if i == N:
#         answer += 1
#         return
#
#     for j in range(N):
#         field[i] = j
#         if checker(i):
#             nqueen(i+1)
# nqueen(0)
# print(answer)


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