# 23.05.05

def converter(n, k):
    over_ten = {"10": 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    num = ""
    if n < 2:
        return str(n)
    while n > 0:
        rest = str(n % k)
        if int(rest) >= 10:
            rest = over_ten[rest]
        num = rest + num
        n //= k
    return num


def solution(n, t, m, p):
    answer = ''
    result = ''
    cnt = 0
    while len(result) < t * m:
        num = converter(cnt, n)
        result = result + num
        cnt += 1
    for i in range(p - 1, len(result), m):
        answer = answer + result[i]
        if len(answer) == t:
            break
    return answer