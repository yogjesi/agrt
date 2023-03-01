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