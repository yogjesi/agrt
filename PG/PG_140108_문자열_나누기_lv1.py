# 23.02.07
# 주의 : 잘 끊기.

def solution(s):
    answer = 0
    i = 2
    while s:
        std = s[0]
        cnt = s.count(std, 0, i)   # 이부분에서 잘못 끊으면 무한루프 도는 현상 발생... 주의하자.
        # cnt = s[:i].count(std)   # 한 줄 위의 코드를 좌측처럼 짜서 틀렸음.
        # print(std, cnt)
        if cnt == i//2:
            s = s[i:]
            answer += 1
            i = 0
        i += 2
    print(answer)
    return answer


solution("banana") # 3나와야 함\
solution("abracadabra")  # 6
