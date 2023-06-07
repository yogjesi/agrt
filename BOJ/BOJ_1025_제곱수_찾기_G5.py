# 23.06.07

# 1. 입력
N, M = map(int, input().split())
arr = []
nums = []
for _ in range(N):
    line = list(map(int, ' '.join(input().split())))
    arr.append(line)
    nums.extend(line)
print(arr)
print(nums)

# 관건은 등차수열을 어떻게 코드로 짜낼지가 관건이로군

# 2. 만들 수 있는 모든 수열 만들어서 담기
# sequences = 수열들을 담을 리스트
sequences = []
# 2-1. freq < M : 역방향
for i in range(2, M):
    for x in range(N*M):
        for y in range(x, N*M, i)
    pass

# 2-2. freq > M : 정방향
for j in range(M+1, N*M):
    pass


# 2-3. freq = 1
for k in range(N):
    sequences.append(arr[k])


# 2-4. freq = M
for c in range(M):
    inst = []
    for r in range(N):
        inst.append(arr[r][c])
    sequences.append(inst)

print(sequences)
