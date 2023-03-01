# lv2

# def solution(n):
#     answer = 0
#     stock = [0]*(n+1)
#     num = 0
#     start = 1
#     for i in range(1, n+2):
#         if num < n:   # num이 수보다 작을 때
#             num += i
#         elif num == n:  # num이 맞아떨어질 때
#             answer += 1
#             num -= start
#             start += 1
#             num += i
#         else: # num이 수를 초과했을 때
#             num -= start
#             start += 1
#         print(num, start)
#
#     return answer

def solution(n):
    answer = 0
    stock = [0]*(n+1)
    num = 0
    start = 1
    i = 1
    while i <= n//2+3:
        print(i, '더할 차례:' ,end=' ')
        if num < n:
            num += i
            i += 1
        elif num == n:
            answer += 1
            num -= start
            start += 1
            num += i
            # print(answer)
            i += 1
        else:
            num -= start
            start += 1
        print(num, start, answer)
    return answer + 1

solution(15)
solution(21)