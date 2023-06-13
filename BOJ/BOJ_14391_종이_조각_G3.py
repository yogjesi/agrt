# 23.06.13
# 아이디어 도출부터 난관... 2가지가 떠오름.
# 첫 째. 길게 자른다.
# 둘 째. 숫자 하나 찍어서 가로 세로 탐색한다.


# 1. 입력부
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, ' '.join(input()).split())))
print(arr)

