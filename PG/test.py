a = [[0, 1, 2, 3],[3, 4, 5, 6],[6, 7, 8, 9], [1, 3, 5, 7]]
print(a[1:3])
b = a[1:3]
for i in range(len(b)):
    b[i] = b[i][1:3]

print(b)