# 23.03.16

import math

def solution(arr):
    for i in range(len(arr)-1):
        f, s = arr[i], arr[i+1]
        result = math.gcd(f, s)
        if result == 1:
            arr[i+1] = f*s
        else:
            arr[i+1] = f*s//result
    answer = arr[-1]
    return answer