max_num = 0, 0

for idx in range(1, 10):
    num = int(input())
    if num > max_num[0]:
        max_num = num, idx

print(max_num[0])
print(max_num[1])