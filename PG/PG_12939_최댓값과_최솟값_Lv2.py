# 22.09.08


# 최댓값과 최솟값

def solution(s):
    nums = list(map(int, s.split()))
    nums.sort()
    min_num, max_num = str(nums[0]), str(nums[-1])
    answer = min_num + ' ' + max_num
    return answer

result = solution("-1 -2 -3 -4")
print(result)