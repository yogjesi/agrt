# 23.05.17
# Four Squares

# 필요한 배열을 생성한 후
# 해당 배열에 있는 숫자들을 4개 이하로 조합시키는 거지
# 그렇게 해서 가장 짧은 게 나오면 탐색 ㄱㄱ
# 약간 DP스럽게 풀어야 하나...?

from itertools import product

n = int(input())                          # 1. 수 받기
length = int(n**(1/2))                    # 2. 루트n 값보다 작은 가장 큰 자연수 구하고
arr = [0]*(length + 1)                    # 2-1. 해당 자연수 길이 + 1 만큼 배열 생성
for i in range(1, length+1):              # 2-2. 배열 안에 인덱스의 제곱수 집어넣기
    arr[i] = i*i
arr.reverse()
                                          # 3. 숫자 조합하기
if n in arr:                              # 3-1. 만일 입력받은 숫자 n 자체가 제곱수일 경우 바로 반환
    print(1)
    exit()




# 아래 코드로는 pypy만 통과
# arr.remove(0)
# answer = 5
# def dfs(num, cnt):
#     global answer
#     if num == n:
#         if answer > cnt:
#             answer = cnt
#         return
#     if cnt >= 3:
#         return
#     for number in arr:
#         if num + number > n:
#             continue
#         dfs(num + number, cnt + 1)
#
# for num in arr:
#     dfs(num, 1)
# print(min(answer, 4))


# 아래 코드는 시간 에러
# std = False                               # 루트 5만은 223.xx 이므로 배열의 최장 길이는 223
# for k in range(2, 4):                     # 3-2. 제곱수 조합 만들어서 구하기(product 사용)
#     result = list(product(arr, repeat=k)) # 근데 이건 아무리 생각해도 시간 초과 날 듯...
#     for nums in result:
#         if sum(nums) == n:
#             std = True
#             print(k)
#             exit()
# if not std:
#     print(4)

