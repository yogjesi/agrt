# 23.05.05
# 테스트 케이스 1번을 통과하는 게 관건이었던 문제.
import math

# 소수인지 판별하기
def isPrimeNum(x):
    if x  < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    l = int(math.sqrt(x)+1)    # 루트로 만들어주는 게 아주 신박했다! 이게 관건.
    for i in range(3, l, 2):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    elems = ""
    # k진수 바꿔주기
    while n > 0:
        rest = str(n % k)
        elems = rest + elems
        n //= k
    # print(elems)
    # 숫자 뽑아내서 numbers에 담기
    numbers = list(map(str, elems.split("0")))
    # print(numbers)
    for number in numbers:
        if number == "" or number == "1":
            continue
        intnum = int(number)
        if isPrimeNum(intnum):
            answer += 1
    return answer