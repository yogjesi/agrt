num = 1
for n in range(3):
    num *= int(input())

num = str(num)

for idx in range(10):
    a = num.count(str(idx))
    print(a)