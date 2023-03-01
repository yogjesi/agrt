# 23.02.10

import collections

def solution(s):
    answer = []
    loc = collections.defaultdict(int)
    for c in range(97, 123):
        loc[chr(c)] = -1
    print(loc)
    return answer