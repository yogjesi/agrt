### 가장 작은 직사각형

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort()   # 정렬
print(points)

must_include = N//2

# 사각형 만들면 그 안에 점 몇 개 있는지 세어주는 거
def how_many_points(start, end):
    (ix, iy) = start
    (jx, jy) = end
    cnt = 0
    for idx in range(N):
        if points[idx][0]>=ix and points[idx][0] <= jx:
            if points[idx][1]>=iy and points[idx][1]<=jy:
                cnt += 1
    return cnt


# min_points : 최소한 들어가야 하는 점 개수
min_points = N//2
# cnt : 사각형 넓이
cnt = 1000000000
for i in range(N):
    s = points[i]
    (sx, sy) = s
    for j in range(i, N):
        e = points[j]
        (ex, ey) = e
        w, h = ex-sx+2, ey-sy+2    # w : width, h = height
        num = how_many_points(s, e)
        if num >= min_points and w*h < cnt:
            cnt = w*h
print(cnt)