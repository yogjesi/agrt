# 23.03.06

def solution(s):
    answer = []
    eli = 0  # eliminated의 약자

    def shorten(num):
        nonlocal eli
        cnt = 0
        for i in range(len(s)):
            if s[i] == '1':
                cnt += 1
            else:
                eli += 1
        result = format(cnt, 'b')
        return result

    con = 0
    while s != '1':
        s = shorten(s)
        con += 1
    answer = [con, eli]
    return answer