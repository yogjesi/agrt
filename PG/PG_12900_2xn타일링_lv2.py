# 23.05.04
# 아 넘나 빡침.... 이런 기본적인 문제를...
# 몇 시간 걸린 거임...? 후....

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    arr = [1, 2]
    for i in range(2, n):
        num = (arr[i - 1] + arr[i - 2]) % 1000000007
        arr.append(num)
    return arr[-1]

    # def roop(num):
    #     nonlocal answer
    #     if num >= n:
    #         if num == n:
    #             answer += 1
    #         return
    #     roop(num+1)
    #     roop(num+2)
    # roop(0)
    return answer