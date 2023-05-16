# 23.05.16

# ...아놔
from itertools import permutations

# 2.가능한가
def isPossible(arr1, arr2, s, b):
    # print('arr1', arr1, 'arr2', arr2)
    stk = 0
    bol = 0
    for i in range(3):
        if arr1[i] == arr2[i]:
            stk += 1
        elif arr2[i] in arr1:
            bol += 1
    if stk == s and bol == b:
        return True
    else:
        return False

N = int(input())

# 거르고 그 안에서 거르고 또 그 안에서 거르고....? 너무 많을까
# 하지만 N은 100 이하니까 가능하지 않을까?
# 그럴 일은 없겠지만 for문 중첩 3번 이하로
# 일단 순열로 만들 수 있는 모든 숫자 구해봅세
nums = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# print(nums)
numbers = []

# 1.
for _ in range(N):
    number, strike, ball = map(int, input().split())
    number = list(' '.join(str(number)).split())  #['1', '2', '3']
    # number = [' '.join(str(number)).split()]
    print(number)
    # print('number', number)
    cnt = 0
    while cnt < len(nums):
        # print(nums[cnt])
        if not isPossible(number, list(map(str, nums[cnt])), strike, ball):
            nums.pop(cnt)
        else:
            cnt += 1
    # print(nums)
print(len(nums))


