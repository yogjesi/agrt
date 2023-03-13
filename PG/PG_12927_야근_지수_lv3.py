# 23.03.11
# 아 lv3이네


# 시간 오버
# def solution(n, works):
#     answer = 0
#     works.sort(reverse=True)
#     for i in range(n):
#         for j in range(len(works)):
#             if j == len(works) - 1:
#                 if works[j] > 0:
#                     works[j] -= 1
#                     break
#                 else:
#                     break
#             if works[j] > works[j + 1] and works[j] > 0:
#                 works[j] -= 1
#                 break
#         # print(works)
#     for i in range(len(works)):
#         answer += works[i] * works[i]
#
#     return answer

# second way

# def solution(n, works):
#     answer = 0
#     for i in range(n):
#         num = max(works)
#         idx = works.index(num)
#         if works[idx] == 0:
#             break
#         works[idx] -= 1
#
#     for j in range(len(works)):
#         answer += works[j] * works[j]
#     return answer

# def solution(n, works):
#     answer = 0
#
#     def heap_sort(array):
#         n = len(array)
#         # heap 구성
#         for i in range(n):
#             c = i
#             while c != 0:
#                 r = (c - 1) // 2
#                 if (array[r] < array[c]):
#                     array[r], array[c] = array[c], array[r]
#                 c = r
#                 # print(array)
#         # 크기를 줄여가면서 heap 구성
#         for j in range(n - 1, -1, -1):
#             array[0], array[j] = array[j], array[0]
#             r = 0
#             c = 1
#             while c < j:
#                 c = 2 * r + 1
#                 # 자식 중 더 큰 값 찾기
#                 if (c < j - 1) and (array[c] < array[c + 1]):
#                     c += 1
#                 # 루트보다 자식이 크다면 교환
#                 if (c < j) and (array[r] < array[c]):
#                     array[r], array[c] = array[c], array[r]
#                 r = c
#         return array
#     works = heap_sort(works)
#     # print(works)
#     for i in range(n):
#         for j in range(len(works)):
#             if j == len(works) - 1:
#                 if works[j] > 0:
#                     works[j] -= 1
#                     break
#                 else:
#                     break
#             if works[j] > works[j + 1] and works[j] > 0:
#                 works[j] -= 1
#                 break
#         # print(works)
#     for i in range(len(works)):
#         answer += works[i] * works[i]
#     return answer



# solution(5, [4, 5, 6, 3, 3, 7, 8, 9, 1, 2, 3, 10, 35, 33, 24, 25, 5, 13])