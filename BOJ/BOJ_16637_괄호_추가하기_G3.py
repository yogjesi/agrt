# 23.06.07

N = int(input())
arr = list(' '.join(input()).split())

stack = []
while arr:
    now = arr.pop(0)
    if now == '*':                                      # 곱셈 로직
        stack.append(int(arr.pop(0)))
    elif now == '+':                                    # 덧셈 로직
        stack[-1] = stack[-1] + int(arr.pop(0))
        if len(stack) > 1:
            n = 1
            for num in stack:
                n *= int(num)
            stack = [n]
    elif now == '-':                                    # 뺄셈 로직
        if len(stack) > 1:
            n = 1
            for num in stack:
                n *= int(num)
        else:
            n = stack[-1]
        # n -= int(arr.pop(0))
        stack = [n]
        if arr[1] == '-':
            if len(arr) > 3 and arr[3] == '-':
                if int(arr[2]) - int(arr[0]) < int(arr[4]) - int(arr[2]):
                    stack[-1] = stack[-1] - int(arr.pop(0))
                else:
                    n1 = int(arr.pop(0))
                    cal = arr.pop(0)
                    n2 = int(arr.pop(0))
                    stack[-1] = stack[-1] - (n1 - n2)
            else:
                n1 = int(arr.pop(0))
                cal = arr.pop(0)
                n2 = int(arr.pop(0))
                stack[-1] = stack[-1] - (n1 - n2)
        else:
            stack[-1] = stack[-1] - int(arr.pop(0))


    else:
        stack.append(int(now))
    # print(stack)

if len(stack) > 1:
    result = 1
    for number in stack:
        result *= number
    print(result)
else:
    print(stack[0])