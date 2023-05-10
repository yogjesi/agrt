# 23.05.10
# 효율성에서 오래 걸린 문제. 프로그래머스 난이도 조절 안 하냐...
# 2432902008176640000
# 근데 진짜 궁금한데 맨 마지막 거 왜 프린트 안 됨...? answer 자체는 되는데...
# 파이참의 문제인가?

# 아무튼 아래의 방법은 효율성도 잘 통과함
def solution(n, k):
    # 정답을 받아줄 배열 answer
    answer = [0] * n
    # 팩토리얼 코드, std는 팩토리얼 결과값(변수 다른 걸로 할 걸...)
    std = 1
    nums = [m for m in range(1, n + 1)]
    for num in range(1, n + 1):
        std *= num
    if std == k:  # 마지막거라면 그냥 빠르게 보내주자
        answer = [x for x in range(n, 0, -1)]
        return answer
    std //= n  # 위에서 n!일 때 고려했으므로, 다시 n을 나눠서 (n-1)!로 만들어 줌.
    idx = 0    # answer에 접근하기 위한 인덱스 값
    while idx < n:
        for i, num in enumerate(nums):
            if (i+1) * std >= k:        # 설명이 푸는 것보다 더 어렵네...
                answer[idx] = num
                nums.remove(num)
                k -= i * std
                idx += 1
                if n - idx > 0:
                    std //= (n - idx)
                break
    return answer


# 아래는 두 개 시간 초과 및 효율성 불통 코드
# def solution(n, k):
#     answer = []
#     cnt = 0
#     def perm(num):
#         nonlocal cnt, answer
#         if len(num) == n:
#             cnt += 1
#             if cnt == k:
#                 answer = num[:]
#             return
#         for i in range(1, n+1):
#             if i not in num :
#                 num.append(i)
#                 perm(num)
#                 num.remove(i)
#     nums = []
#     perm(nums)
#     print(answer)
#     return answer
solution(20, 2432902008176640000)
solution(3, 5)
solution(5,100)