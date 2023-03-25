# 23.03.25

def solution(n,a,b):
    answer = 1
    cnt = 0
    while n != 1:
        n = n//2
        cnt += 1
    for i in range(1, cnt+1):
        if a%2 == 1:
            a = a//2 + 1
        else:
            a = a//2
        if b%2 == 1:
            b = b//2 + 1
        else:
            b = b//2
        if (a+1 == b) and (b%2==0):
            answer = i + 1
            break
        elif (b+1 == a) and (a%2==0):
            answer = i + 1
            break
        # print(a, b)
    return answer

solution(8, 4, 7)