# 22.08.26
# 정렬


# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

# print(A, B)

for n in range(K):
    if A[n] < B[n]:
        A[n], B[n] = B[n], A[n]
    else:
        break

print(sum(A))