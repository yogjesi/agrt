import sys

N = int(sys.stdin.readline())
nums = [0]*10001
for _ in range(N):
    num = int(sys.stdin.readline())
    nums[num] += 1

for num in range(len(nums)):
    if nums[num] != 0:
        for _ in range(nums[num]):
            print(num)