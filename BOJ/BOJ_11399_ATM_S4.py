# 정렬, 그리디

# 우선순위 큐? 맞을까?

N = int(input())
time = list(map(int, input().split()))

time.sort(reverse=True)
time.insert(0, 0)

answer = 0
for idx in range(1, N+1):
    answer += idx * time[idx]

print(answer)