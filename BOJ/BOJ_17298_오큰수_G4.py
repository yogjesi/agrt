# 23.05.10




# stack이라는데 stack 안 씀
N = int(input())
answer = [-1]*N
numbers = list(map(int, input().split()))

for i in range(N-1, -1, -1):
    for j in range(i-1, -1, -1):
        if numbers[j] < numbers[i]:
            answer[j] = numbers[i]
        else:
            break
for num in answer:
    print(num, end=" ")
