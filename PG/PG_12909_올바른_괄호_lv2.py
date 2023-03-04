#
# 23.03.04
# def solution(s):
#     answer = True
#     stack = []
#
#     if len(s) % 2 != 0:  # 짝수 아니면 어차피 안 됨
#         return False
#
#     if s[0] == '(':  # 첫번째 거 넣고 시작할 것임
#         stack.append(s[0])
#         s = s[1:]
#     else:
#         return False
#
#     while len(s) != 0:
#         if s[0] == ')':
#             if stack == []:
#                 return False
#             else:
#                 stack.pop()
#                 s = s[1:]
#         else:
#             stack.append('(')
#             s = s[1:]
#     if stack == []:
#         return True
#     else:
#         return False

# second
from collections import deque

def solution(s):
    stack = deque()
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


result = solution('(())(())()((()(()))')

print(result)