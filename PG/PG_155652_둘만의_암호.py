# 이거 레벨 1인데 왜 자꾸 틀리냐... 아놔


# 아래는 런타임 에러 나는 노래
# def solution(s, skip, index):
#     answer = ''
#     alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
#                 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     for i in range(len(skip)):
#         if skip[i] in alp:
#             alp.remove(skip[i])
#     ns = []
#     l = len(alp) - 1
#     for j in range(len(s)):
#         inst = alp.index(s[j]) + index
#         if inst > l:
#             inst -= (l+1)
#         ns.append(alp[inst])
#     answer = ''.join(ns)
#     return answer

import collections

def solution(s, skip, index):
    answer = ''

    return answer