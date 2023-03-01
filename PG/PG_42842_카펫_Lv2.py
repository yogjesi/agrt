# 22.08.24


def solution(brown, yellow):
    all_grid = brown + yellow
    half = brown//2
    max_w = half//2
    for i in range(1, max_w + 2):
        w = half - i + 1
        h = i + 1
        yw = w-2
        yh = h-2
        if yw*yh == yellow:
            return [w, h]
            break