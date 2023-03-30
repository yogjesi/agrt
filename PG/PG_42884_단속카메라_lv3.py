# 23.03.30

def solution(routes):
    answer = 0
    cam = -30001
    routes = sorted(routes, key=lambda x:x[1])
    # print(routes)
    for x, y in routes:
        if cam < x:
            answer += 1
            cam = y
    return answer