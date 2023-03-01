T = int(input())

for tc in range(T):
    ans = input()
    cnt = 1
    score = 0
    for idx in range(len(ans)):
        if ans[idx] == 'O':
            score += cnt
            cnt +=1
        else:
            cnt = 1
    print(score)
