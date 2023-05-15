# 23.05.15

# A명의 사람이 게임을 진행, T번째 S를 외친 사람을 찾자
A = int(input())
T = int(input())
S = int(input())

cnt_dict = {0:0, 1:0}

result = []
cnt = 1
while cnt_dict[S] < T:          # 1회만큼 돌려 나옴. 안에서 끊어도 되긴 하지만.. 귀찮...
    result.extend([0, 1, 0, 1])
    instA = [0]*(cnt + 1)
    instB = [1]*(cnt + 1)
    result.extend(instA)
    result.extend(instB)
    cnt_dict[0] += (2 + cnt + 1)
    cnt_dict[1] += (2 + cnt + 1)
    cnt += 1

res_dict = {0:0, 1:0}
for i in range(len(result)):
    res_dict[result[i]] += 1
    if res_dict[S] == T:
        answer = i%A
        break
print(answer)