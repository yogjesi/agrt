# 23.05.05
# lv3 치곤 쉬웠음, 다만 슬라이싱 범위 주의해야 함
# idea :  기지국 사이에 전파가 도달하지 않는 구간을 구하고
# 각 구간을 커버리지로 나눠서 추가할 갯수 구함
# N이 매우 크기 때문에 O(N)이하로 처리하기 위해 노력함
import math

def solution(n, stations, w):
    answer = 0
    coverage = w*2+1
    start = 0
    if stations[-1] - 1 + w < n-1:
        stations.append(n + 1 + w)
    for station in stations:
        end = station - 1 - w
        l = end - start
        answer += math.ceil(l/coverage)
        start = end + 2 * w + 1
    return answer