# 23.05.04
# greedy
import math
from heapq import heappush, heappop
# N개의 마을, X[i] : 마을, A[i] : 사람 수
# 3 번째 방법
N = int(input())
info = []
front, back, total = 0, 0, 0
for _ in range(N):
    x, a = map(int, input().split())
    info.append((x, a))
    back += a
info.sort()
s, e = info[0][0], info[-1][0] 
# 3-2



# 3-1
# nextX, nextA = info.pop(0)
# back -= nextA
# print(back)
# total += back
# last = 0
# for i in range(s, e+2):
#     print(i, "번 째")
#     if last >= total or total < 0:
#         print(i-1)
#         break
#     print("front", front, "now", nextA, "back", back)
#     last += front
#     total -= back
#     print("last", last, "total", total)
#     if nextX == i:
#         front += nextA
#         nextX, nextA = info.pop(0)
#         back -= nextA
    # print("next", nextA)




#  2번째 방법
# N = int(input())
#
# info = []
# front, now, back = 0, 0, 0
# for _ in range(N):
#     x, a = map(int, input().split())
#     info.append((x, a))
#     back += a
# info.sort()
# answer = 0
# for x, a in info:
#     now = a
#     back -= a
#     if now >= front and now+front >= back:
#         print(x)
#         break
#     front += a




# 1번째 방법 : 3%에서 시간초과
# N = int(input())
#
# X = []
# A = []
# minVal = math.inf
# for _ in range(N):
#     x, a = map(int, input().split())
#     X.append(x)
#     A.append(a)
#
# answer = 0
# for i in X:
#     result = 0
#     for x, a in zip(X, A):
#         dist = abs(x-i)
#         result += dist*a
#     if minVal > result:
#         minVal = result
#         answer = i
# print(answer)