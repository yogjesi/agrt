nums = []
for idx in range(10):
    num = int(input())
    a = num%42
    nums.append(a)

nums = set(nums)
print(len(nums))