# 23.05.12
# 아이디어는 있으나 구현하는데서 애먹어서
# 다른 코드 참조함
# 쉬울 거라 생각했는데... 또르륵...

def solution(order):
    answer = 0
    n = len(order)
    stack = []
    i = 1
    while i < n+1:
        stack.append(i)    # 일단 스택에 냅다 집어넣고 생각하기
        while stack[-1] == order[answer]:
            answer += 1
            stack.pop()
            if not stack:
                break
        i += 1
    return answer