# def solution(x, y, n):
#     answer = -1
#     def calc(num, cnt):
#         nonlocal answer
#         if num == y:
#             if answer == -1:
#                 answer = cnt
#             elif answer > cnt:
#                 answer = cnt
#             return
#         elif num > y:
#             return
#
#         calc(num*3, cnt+1)
#         calc(num*2, cnt+1)
#         calc(num+n, cnt+1)
#
#         for i in range(3):
#             if i == 0:
#                 num += n
#             elif i == 1:
#                 num *= 2
#             elif i == 2:
#                 num *= 3
#             if num > y:
#                 continue
#             calc(num, cnt+1)

    # calc(x, 0)
    # return answer

# 2nd way

from collections import deque

def solution(x, y, n):
    answer = -1
    q = deque()
    q.append((0, x))

    check = [0]*1000001

    while q:
        # print('1', q)
        cnt, now = q.popleft()
        if now == y:
            answer = cnt
            break
        if now > y:
            continue
        cnt += 1

        first = now + n
        second = now * 2
        third = now * 3

        if third <= y and check[third] == 0:
            q.append((cnt, third))
            check[third] = 1
        if second <= y and check[second] == 0:
            q.append((cnt, second))
            check[second] = 1
        if first <= y and check[first] == 0:
            q.append((cnt, first))
            check[first] = 1

        # print('2', q)
    return answer


# result = solution(10, 40, 30)
# print(result)
result = solution(1, 1000000, 1)
print(result)