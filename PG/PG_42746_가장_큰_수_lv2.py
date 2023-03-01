# 정렬_가장 큰 수
# 2022.10.27

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer



solution([6, 10, 2])
solution([3, 30, 34, 5, 9])