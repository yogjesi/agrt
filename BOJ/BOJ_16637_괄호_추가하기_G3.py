# 23.06.07
# 삼성 A형 기출

# https://velog.io/@weenybeenymini/%EB%B0%B1%EC%A4%80-16637%EB%B2%88-%EA%B4%84%ED%98%B8-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0


import sys

n = int(input())
s = input()
result = -1 * sys.maxsize                       # 최소 처리

def myOperator(num1, oper, num2):               # 계산용 코드
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2

# index 현재 위치, value는 계산한 값
def dfs(index, value):                          # 탐색 : dfs
    global result

    if index == n - 1:                          # base case에 도달하면(마지막 인덱스에 도달하면)
        result = max(result, value);            # 값을 비교해서 업데이트
        return

    if index + 2 < n:                           # 인덱스가 2개 더 있다는 건 연산자와 숫자가 하나씩 있단 것
        dfs(index + 2, myOperator(value, s[index + 1], int(s[index + 2])))

    if index + 4 < n:                           # 인덱스가 4개 더 있다는 건 [연산자] [숫자] [연산자] [숫자], 근데 이제 여기에 괄호를 넣겠단 거
        dfs(index + 4, myOperator(value, s[index + 1], myOperator(int(s[index + 2]), s[index + 3], int(s[index + 4]))))

dfs(0, int(s[0]))
print(result)

# 연산과 탐색을 분리하면 생각하는 게 좀 더 깔끔할 수 있다는 걸 깨달음


# N = int(input())
# arr = list(' '.join(input()).split())
#
# stack = []
# while arr:
#     now = arr.pop(0)
#     if now == '*':                                      # 곱셈 로직
#         stack.append(int(arr.pop(0)))
#     elif now == '+':                                    # 덧셈 로직
#         stack[-1] = stack[-1] + int(arr.pop(0))
#         if len(stack) > 1:
#             n = 1
#             for num in stack:
#                 n *= int(num)
#             stack = [n]
#     elif now == '-':                                    # 뺄셈 로직
#         if len(stack) > 1:
#             n = 1
#             for num in stack:
#                 n *= int(num)
#         else:
#             n = stack[-1]
#         # n -= int(arr.pop(0))
#         stack = [n]
#         if arr[1] == '-':
#             if len(arr) > 3 and arr[3] == '-':
#                 if int(arr[2]) - int(arr[0]) < int(arr[4]) - int(arr[2]):
#                     stack[-1] = stack[-1] - int(arr.pop(0))
#                 else:
#                     n1 = int(arr.pop(0))
#                     cal = arr.pop(0)
#                     n2 = int(arr.pop(0))
#                     stack[-1] = stack[-1] - (n1 - n2)
#             else:
#                 n1 = int(arr.pop(0))
#                 cal = arr.pop(0)
#                 n2 = int(arr.pop(0))
#                 stack[-1] = stack[-1] - (n1 - n2)
#         else:
#             stack[-1] = stack[-1] - int(arr.pop(0))
#
#
#     else:
#         stack.append(int(now))
#     # print(stack)
#
# if len(stack) > 1:
#     result = 1
#     for number in stack:
#         result *= number
#     print(result)
# else:
#     print(stack[0])