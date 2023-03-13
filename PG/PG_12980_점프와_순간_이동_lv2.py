# 23.03.13

def solution(n):
    ans = 0
    while n != 0:
        rest = n%2
        if rest == 1:
            ans += 1
        n = n//2
    return ans

# 겁나 쉬움