# 22.08.31
# 정렬 연습용


# 그냥 sort 쓰면 안 되는 문제
# 퀵 아니면 병합 정렬 쓰는 건가? 근데 sort가 병합이라며...


# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 수가 주어진다.
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다.
# 수는 중복되지 않는다.
import sys

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
# print(nums)


# 1. quick 정렬
# def quick(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr)//2]
#     tail = arr[0:len(arr)//2] + arr[len(arr)//2+1:]
#
#     left_side = [x for x in tail if x <= pivot]
#     right_side = [y for y in tail if y > pivot]
#     return quick(left_side) + [pivot] + quick(right_side)
#
# result = quick(nums)

# 2. python 라이브러리

nums.sort()

for num in nums:
    print(num)