# 23.04.05
# 일부 실패, 일부 성공

from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    # print(scoville)
    while len(scoville) > 1:
        scv1 = heappop(scoville)
        scv2 = heappop(scoville)
        nscv = scv1 + (scv2 * scv2)
        heappush(scoville, nscv)
        std = True
        for food in scoville:
            if food < K:
                std = False
                break
        if std == True:
            answer += 1
            break
        else:
            answer += 1

    return answer



# 2022.08.12
# Heap(힙)

# def solution(scoville, K):
#     scoville.sort()
#     if scoville[0] >= K:
#         answer = 0
#     else:
#         cnt = 1
#         while cnt < len(scoville):
#             new_food = scoville[0] + scoville[1]*2
#             scoville = scoville[2:]
#             scoville.append(new_food)
#             scoville.sort()
#             if scoville[0]>=K:
#                 answer = cnt
#                 break
#             else:
#                 cnt += 1
#     print(answer)
#     return answer


solution([1, 2, 3, 9, 10, 12], 7)