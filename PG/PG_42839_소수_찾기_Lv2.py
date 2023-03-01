# 22.08.24
# 완전 탐색

from itertools import permutations


# 순열 라이브러리 가져오기

# isPrime : 소수 검사용
def isPrime(number):
    for n in range(2, number):
        if number % n == 0:  # 나누어 떨어지면 소수가 아님
            return False
    # 다 통과했으면 소수라는 것이므로
    return True

# makeNums : 숫자 조합해서 만들기
def makeNums(arr):
    all_nums = []
    for m in range(1, len(arr) + 1):
        perm = list(permutations(arr, m))
        all_nums.extend(perm)

    nums = []
    for k in range(len(all_nums)):
        nums.append(int(''.join(all_nums[k])))

    return nums

# 본 코드
def solution(numbers):
    num_list = []
    # 숫자로 바꿔서 담아줌
    for i in range(len(numbers)):
        num_list.append(numbers[i])

    # 1. 조합하고
    nums = makeNums(num_list)
    nums = list(set(nums))      # 중복 제거를 해줘야 함!!!!

    # 2. 검사하고
    cnt = 0
    for num in nums:
        if num >= 2:
            if isPrime(num) == True:
                cnt += 1
    return cnt


result = solution("011")
print(result)