# 23.05.18

# Way 1. 아래는 통과
H, W = map(int, input().split())
N = int(input())
stickers = []
for _ in range(N):
    r, c = map(int, input().split())
                                           # 1. 애초에 안 되는 건 걸러서 stickers에 담기
    if r*c > H*W:                          # 1-1. 스티커 면적이 모눈종이 면적보다 더 클 경우
        continue
    if max(r, c) > max(H, W):              # 1-2. 스티커의 긴 변 길이가 모눈종이 긴 변이 더 클때
        continue
    if min(r, c) > min(H, W):              # 1-3. 작은 길이가 비어져나갈 때
        continue
    stickers.append((r,c))
stickers.sort(key=lambda x:-(x[0]*x[1]))   # 2. 면적이 넓은 순서로 정렬 (아 근데 어차피 다 비교할 거면 이거 안해도 될 듯?)
answer = 0                                 # 3. answer 기본 값은 0
while stickers:                            # 4. stickers 전부 돌면서 비교해주기 (조합(combinations) 써도 될 거 같긴 함)
    a, b = stickers.pop(0)                 # 4-1. 가장 앞의 것을 뽑아내고 (여기서는 deque를 써도 빠르지 않을까...)
    for c, d in stickers:                  # 4-2. 스티커스에서 나머지 스티커 한 개씩 꺼내어 돌리는데, 조합법 4가지가 있음
        arr = []
        w1, h1 = (a+c), max(b, d)  # case 1
        arr.append((w1, h1))
        w2, h2 = (a+d), max(b, c)  # case 2
        arr.append((w2, h2))
        w3, h3 = (b+c), max(a, d)  # case 3
        arr.append((w3, h3))
        w4, h4 = (b+d), max(a, c)  # case 4
        arr.append((w4, h4))
        for w, h in arr:
            if max(w, h) <= max(H, W) and min(w, h) <= min(H, W):
                if (a*b + c*d) > answer:
                    answer = a*b + c*d
print(answer)


#  Way 2. 아래는 조합 사용했을 때
# from itertools import combinations
#
# H, W = map(int, input().split())
# N = int(input())
# stickers = []
# for _ in range(N):
#     r, c = map(int, input().split())
#                                            # 1. 애초에 안 되는 건 걸러서 stickers에 담기
#     if r*c > H*W:                          # 1-1. 스티커 면적이 모눈종이 면적보다 더 클 경우
#         continue
#     if max(r, c) > max(H, W):              # 1-2. 스티커의 긴 변 길이가 모눈종이 긴 변이 더 클때
#         continue
#     if min(r, c) > min(H, W):              # 1-3. 작은 길이가 비어져나갈 때
#         continue
#     stickers.append((r,c))
# stickers.sort(key=lambda x:-(x[0]*x[1]))
# answer = 0
# pairs = list(combinations(stickers, 2))
# # print(pairs)
# while pairs:
#     (a, b), (c, d) = pairs.pop(0)
#     arr = []
#     w1, h1 = (a+c), max(b, d)  # case 1
#     arr.append((w1, h1))
#     w2, h2 = (a+d), max(b, c)  # case 2
#     arr.append((w2, h2))
#     w3, h3 = (b+c), max(a, d)  # case 3
#     arr.append((w3, h3))
#     w4, h4 = (b+d), max(a, c)  # case 4
#     arr.append((w4, h4))
#     for w, h in arr:
#         if max(w, h) <= max(H, W) and min(w, h) <= min(H, W):
#             if (a*b + c*d) > answer:
#                 answer = a*b + c*d
# print(answer)