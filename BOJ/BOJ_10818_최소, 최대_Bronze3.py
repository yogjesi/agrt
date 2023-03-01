T = int(input())

arr = list(map(int, input().split()))
print(arr)

min_num = 1000000
max_num = -1000000

for idx in range(T):
    if arr[idx] > max_num:
        max_num = arr[idx]
    if arr[idx] < min_num:
        min_num = arr[idx]

print(min_num, max_num)