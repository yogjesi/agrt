# 23.04.23

def solution(s):
    answer = 0

    def check(arr):
        stack = []
        for k in range(len(arr)):
            if arr[k] in ["{", "[", "("]:
                stack.append(arr[k])
                continue
            if not stack:
                return 0
            if arr[k] == "}" and stack[-1] == "{":
                stack.pop()
            elif arr[k] == "]" and stack[-1] == "[":
                stack.pop()
            elif arr[k] == ")" and stack[-1] == "(":
                stack.pop()
        if not stack:
            return 1
        else:
            return 0

    for i in range(len(s)):
        ns = s[i:] + s[:i]
        # print(ns)
        cnt = check(ns)
        answer += cnt

    return answer