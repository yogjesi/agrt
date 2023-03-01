# 92쪽

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
result = [-1]*M

# 첫번째 방법
# cnt = 0
# for i in range(M):
#     if cnt == K:
#         result[i] = numbers[-2]
#         cnt = 0
#         continue
#     result[i] = numbers[-1]
#     cnt += 1
# print(sum(result))


# 두 번째 방법
first = numbers[-1]
second = numbers[-2]

num_fst = M // (K+1) * K + M % (K+1)
num_scd = M // (K+1)

answer = first * num_fst + second * num_scd
print(answer)


