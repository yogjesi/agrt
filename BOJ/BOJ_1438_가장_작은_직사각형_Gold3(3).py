### 가장 작은 직사각형


# 반례 케이스
# 6
# 1 1
# 2 3
# 3 2
# 1 5
# 5 5
# 5 1
# 답 : 16

N = int(input())
points = []
x_points = []
y_points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    x_points.append(x)
    y_points.append(y)

points.sort()   # 정렬

# 사각형 만들면 그 안에 점 몇 개 있는지 세어주는 거
def how_many_points(start, end):
    (ix, iy) = start
    (jx, jy) = end
    point_cnt = 0
    for idx in range(N):
        if points[idx][0]>=ix and points[idx][0] <= jx:
            if points[idx][1]>=iy and points[idx][1]<=jy:
                point_cnt += 1
    return point_cnt

# 격자? 만들기
grid_w = max(x_points) - min(x_points)
grid_h = max(y_points) - min(y_points)

# min_points : 최소한 들어가야 하는 점 개수
# cnt : 사각형 넓이
min_points = N/2
cnt = 1000000000
(sx, sy) = (min(x_points), min(y_points))
(ex, ey) = (min(x_points), min(y_points))

# 1. 죽이 되든 밥이 되든 다 돌아보자:
# 그러나 아니나 다를까 시간초과 ㅠㅠ
for i in range(grid_w+1):
    for j in range(grid_h+1):
        s = (min(x_points)+i, min(y_points)+j)
        for m in range(i, grid_w+1):
            for n in range(grid_h+1):
                e = (ex+m, ey+n)
                # print(s, e)
                w, h = e[0]-s[0]+2, abs(e[1]-s[1])+2
                if w*h<cnt and how_many_points(s, e) >= min_points:
                    cnt = w*h
        if y_points.count(s[1]) <= 1:
            break

print(cnt)