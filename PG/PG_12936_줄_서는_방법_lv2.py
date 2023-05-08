# 23.05.08

# 아래는 두 개 시간 초과 및 효율성 불통 코드
def solution(n, k):
    answer = []
    cnt = 0
    def perm(num):
        nonlocal cnt, answer
        if len(num) == n:
            cnt += 1
            if cnt == k:
                answer = num[:]
            return
        for i in range(1, n+1):
            if i not in num :
                num.append(i)
                perm(num)
                num.remove(i)
    nums = []
    perm(nums)
    return answer