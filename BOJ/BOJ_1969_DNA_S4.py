# 23.05.15

N, M = map(int, input().split())

# 그냥 각 열에 가장 많은 문자 구하면 될 듯? 심플하군

# 1. 일단 알파벳 순서도 관련 있으니까 A, C, G, T 순서로 몇 개씩 존재하는 지 받을 것임.
answer = [[0, 0, 0, 0] for _ in range(M)]
all = []
for i in range(N):
    inst = list(' '.join(input()).split())
    for j in range(M):
        if inst[j] == 'A':
            answer[j][0] += 1
        elif inst[j] == 'C':
            answer[j][1] += 1
        elif inst[j] == 'G':
            answer[j][2] += 1
        else:
            answer[j][3] += 1
    all.append(inst)


# 2. 문자열 구하기
result = ''
for k in range(M):
    idx = 0
    for c in range(4):
        if answer[k][c] > answer[k][idx]:
            idx = c
    if idx == 0:
        result = result + 'A'
    elif idx == 1:
        result = result + 'C'
    elif idx == 2:
        result = result + 'G'
    else:
        result = result + 'T'
print(result)

# 3. 다른 개수 구하기
cnt = 0
for r in range(N):
    for c in range(M):
        if all[r][c] != result[c]:
            cnt += 1
print(cnt)