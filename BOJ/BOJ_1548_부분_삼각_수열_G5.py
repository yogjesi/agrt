# 23.06.07
import sys


# 1. 입력부
N = int(input())
arr = list(map(int, input().split()))

# 2. 만일 배열의 원소 개수가 3보다 작다면 바로 리턴
if len(arr) < 3:
    print(len(arr))
    sys.exit()

# 세 번 째 방법 : 약간 슬라이딩-윈도우 느낌의 문제인가? 투포인터라고 해야 하나?
arr.sort()                                          # 정렬 : "(제일 작은 수) + (다음 작은 수) > (다른 수)"인지 차례로 비교하기 위함
answer = 0                                          # 정답은 0으로 초기화
i = 2                                               # i는 세 번째로 작은 수의 인덱스 값부터 차례로 올라가므로 2로 초기화
# 3. 배열 탐색
while len(arr)>= 3 and i < len(arr):
    if arr[0] + arr[1] <= arr[i]:                   # 3-1. 초기화 조건 : 작은 거 두 개의 합이 하나의 수 보다 작다면 부분 삼각 수열의 조건을 만족하지 못함
        # print("before", arr, end=" ")
        if len(arr[:i]) > answer:                   # 3-1-1. 배열의 처음부터 현재까지의 길이가 기존에 저장된 answer 값보다 크다면
            answer = len(arr[:i])                   # answer 값을 업데이트 함
            # print("answer", arr[:i], end=" ")
        arr.pop(0)                                  # 3-1-2. 배열의 첫 번재 수를 빼고 i (인덱스) 값을 초기화시킴
        i = 2
        # print("after", arr)
    else:                                           # 3-2. 현재까지의 수열이 부분 삼각 수열을 만족한다면
        i += 1                                      # 계속해서 i의 값을 늘려나감
# 4. 정답 출력
if len(arr) >= 3 and arr[0] + arr[1] > arr[-1]:     # 마지막 배열이 카운트되지 않을 경우 대비함
    print(max(answer, len(arr)))
else:
    print(answer)




#두 번 째 방법
# arr.sort(reverse=True)
# if len(arr) < 3:
#     print(len(arr))
#     sys.exit()
# # if len(arr) == 3 and arr[0] >= arr[1] + arr[2]:      # 이부분 살짝 하드코딩...
# #     print(2)
# #     sys.exit()
# # print(arr)
# answer = 0
# i = 2
# coms = []
# while i < len(arr):
#     if arr[0] >= arr[i-1] + arr[i]:
#         if answer < len(arr[:i]):
#             coms.append(arr[:i])
#         arr.pop(0)
#         i = 2
#     else:
#         i += 1
# # print(coms)
#
# result = 0
# for com in coms:
#     if len(com) < 3 and len(com) > result:
#         result = len(com)
#         continue
#     com.sort()
#     while len(com) >= 3:
#         if com[0] + com[1] > com[-1]:
#             if result < len(com):
#                 result = len(com)
#                 break
#         if com[-3] + com[-2] <= com[-1]:
#             com.pop(-1)
#         else:
#             com.pop(0)
#     if len(com ) > result:
#         result = len(com)
# print(result)


# 첫 번 째 방법 : 실패. 근데 왜 실패했는지 알겠음.
# arr.sort()
# if len(arr) < 3:                    # 삼각형이 안 만들어지는 케이스
#     print(len(arr))
#     sys.exit()
# while len(arr) >= 3:
#     if arr[0] + arr[1] > arr[-1]:   # 정상적인 상황?
#         break
#     if arr[-3] + arr[-2] <= arr[-1]: # 정상적이지 않은 상황
#         arr.pop(-1)
#     else:
#         arr.pop(0)
# print(len(arr))