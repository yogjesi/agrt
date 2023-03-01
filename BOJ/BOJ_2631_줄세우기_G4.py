
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
# print(nums)
best = []

order = [0]*N
order[0] = 1

for k in range(1, N):
    for n in range(k-1, -1, -1):
        if nums[n] < nums[k] and order[k] <= order[n]:
            order[k] = order[n] + 1
    if order[k] == 0:
        order[k] = 1
print(order)

answer = max(order)
print(N-answer)