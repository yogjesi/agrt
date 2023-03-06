# 23.03.05
# 산술평균인지 기하평균인지 여튼 수학적으로 접근해서 풀었음!

def solution(n, s):
    answer = []
    num = s // n
    last = s % n
    if num <= 0:
        return [-1]

    answer = [num] * n
    for i in range(last):
        answer[i] += 1
    answer.sort()

    return answer

# 테스트 1 〉	통과 (0.20ms, 10.5MB)
# 테스트 2 〉	통과 (0.60ms, 10.6MB)
# 테스트 3 〉	통과 (0.71ms, 10.5MB)
# 테스트 4 〉	통과 (0.48ms, 10.7MB)
# 테스트 5 〉	통과 (0.63ms, 11.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)

# 아래는 sort 없이, 아주 약간 더 효율적임.
# def solution(n, s):
#     answer = []
#     num = s // n
#     last = s % n
#     if num <= 0:
#         return [-1]
#
#     answer = [num] * n
#     for i in range(n - 1, n - last - 1, -1):
#         answer[i] += 1
#
#     return answer

# 테스트 1 〉	통과 (0.17ms, 10.4MB)
# 테스트 2 〉	통과 (0.58ms, 10.6MB)
# 테스트 3 〉	통과 (0.44ms, 10.6MB)
# 테스트 4 〉	통과 (0.44ms, 10.6MB)
# 테스트 5 〉	통과 (0.38ms, 11MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)