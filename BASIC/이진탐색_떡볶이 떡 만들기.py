# 201쪽

# 4 6
# 19 15 10 17

# 1. 내가 짠 코드
# N, M = map(int, input().split())
# # 떡 리스트?
# ddeok = list(map(int, input().split()))
#
# l = max(ddeok)
#
# arr = [0]*l
# for d in ddeok:
#     for i in range(d):
#         arr[i] += 1
#
# cnt = 0
# e = l
# s = 0
# while M > cnt:
#     s += 1
#     cnt = sum(arr[e-s:])
# print(l-s)


# 2. 예시 코드
N, M = map(int, input().split())
ddeok = list(map(int, input().split()))

s = 0
e = max(ddeok)

result = 0
while (s <= e):
    total = 0
    mid = (s + e) // 2
    for x in ddeok:
        if x > mid:
            total += x - mid
    if total < M:
        e = mid - 1
    else:
        result = mid
        s = mid + 1

print(result)