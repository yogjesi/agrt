# 예전에 풀어놨는데 효율성에서 다 떨어진 거
# def solution(s):
#     sol = list(''.join(s))
#
#     if len(sol)%2 !=0:
#         return 0
#
#     stack = []
#     while sol:
#         if stack == []:   #stack이 비어있으면
#             if len(sol) > 1:
#                 if sol[0] != sol[1]:
#                     stack.append(sol.pop(0))
#                 else:
#                     sol = sol[2:]
#             else:
#                 stack.append(sol.pop(0))
#         else:   #stack이 비어있지 않으면
#             if stack[-1] == sol[0]:
#                 stack.pop(-1)
#                 sol.pop(0)
#             else:
#                 if len(sol) > 1:
#                     if sol[0] != sol[1]:
#                         stack.append(sol.pop(0))
#                     else:
#                         sol = sol[2:]
#                 else:
#                     stack.append(sol.pop(0))
#
#     if stack != []:
#         return 0
#     else:
#         return 1


# second way

# def solution(s):
#     stack = []
#     words = []
#     words.extend(s)
#     # print(words)
#     while words:
#         if not stack:
#             stack.append(words[0])
#             words = words[1:]
#             continue
#         if stack[-1] == words[0]:
#             stack.pop()
#             words = words[1:]
#             continue
#         stack.append(words[0])
#         words = words[1:]
#
#     if stack or words:
#         return 0
#     else:
#         return 1

# third way
from collections import deque

# def solution(s):
#     stack = []
#     words = []
#     while words:
#         if not stack:
#             stack.append(words[0])
#             words = words[1:]
#             continue
#         if stack[-1] == words[0]:
#             stack = stack[:-1]
#             words = words[1:]
#             continue
#         stack.append(words[0])
#         words = words[1:]
#
#     if stack or words:
#         return 0
#     else:
#         return 1

def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
            continue
        if stack[-1] == s[i]:
            stack.pop()
            continue
        stack.append(s[i])

    if stack:
        return 0
    else:
        return 1