# 22.08.26
# 정렬 (아무 정렬...)
# 기본 내장함수 쓰기...

# 3
# 15
# 27
# 12

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
print(arr)