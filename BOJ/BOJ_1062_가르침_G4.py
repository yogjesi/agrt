# 23.07.14


# way 2.
import sys
from itertools import combinations

N, K = map(int, input().split())

if K < 5:
    print(0)
    sys.exit()
K -= 5

def convert(x):
    return ord(x) - ord('a')

def convert2(arr):
    result = 0
    for a in arr:
        result |= (1 << a)
    return result

chars = set([convert(n) for n in ['a', 'n', 't', 'i', 'c']])

base = 0
for i in chars:
    base |= (1 << i)

arr = [set(map(convert, input().strip())) for _ in range(N)]

arr_2 = [convert2(a) for a in arr]
picks = set().union(*arr) - chars
answer = 0
if len(picks) <= K:
    print(N)
else:
    for c in combinations(picks, K):
        temp = base
        for i in c:
            temp |= ( 1<< i)
        temp ^= (1 << 26) - 1
        answer = max(answer, sum(1 if (temp&a) == 0 else 0 for a in arr_2))
    print(answer)

# 1. 아래는 시간 초과 코드
# antic : 기본 다섯글자는 할 수 있어야 단어 읽을 수 있음
# anta + x + tica
# import sys
# from itertools import combinations
#
# N, K = map(int, input().split())
#
# if K < 5:
#     print(0)
#     sys.exit()
#
# char = ['a', 'n', 't', 'i', 'c']
# K -= 5
#
# words = []
# rests = set()
# for i in range(N):
#     word = input()
#     new_word = word[4:-4]
#     inst = []
#     for w in new_word:
#         inst.append(w)
#         if w in char:
#             continue
#         else:
#             rests.add(w)
#     words.append(set(inst))
# rests = list(rests)
# answer = 0
# combi = list(combinations(rests, K))
# for picks in combi:
#     score = 0
#     picks = set(picks)
#     picks.update(char)
#     for word in words:
#         test = picks|word
#         if picks == test:
#             score += 1
#     if score > answer:
#         answer = score
# print(answer)