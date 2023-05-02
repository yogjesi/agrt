# 23.05.01

# N : 센서 갯수, K : 센서 집중국 갯수
N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
dist = []
for i in range(1, N):
    dist.append(sensors[i] - sensors[i-1])
dist.sort()
j = len(dist)
dist = dist[:j-K+1]
answer = sum(dist)
print(answer)