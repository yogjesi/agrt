# 23.07.02


# 세 번째 방법 : 몰루... 이게 매나 DFS인가?
# N = int(input())
# answer = -1
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# i = 0
# while nums[-1] <= 9876543210 or i < len(nums):
#     now = nums[i]
#     str_now = str(now)
#     for j in range(10):
#         if j > int(str_now[0]):
#             num = int(str(j) + str_now)
#             nums.append(num)
#     i += 1
# nums.sort()
# if N > len(nums):
#     print(-1)
# else:
#     print(nums[N-1])

# 두 번째 방법 : DFS
N = int(input())
nums = []  # 그냥 0~9
result = set()   # 줄어드는 수 모음
def make_num():
    global nums, result
    if nums:
        result.add(int(''.join(map(str, nums))))

    for i in range(10):
        if not nums or nums[-1] > i:
            nums.append(i)
            make_num()
            nums.pop()

make_num()
result = list(result)
result.sort()
if N <= len(result):
    print(result[N-1])
else:
    print(-1)



# 첫 번째 방법 : 아마도 시간 초과 날 듯
# N = int(input())
# answer = -1
# cnt = 0
# nums = []
# num = 0
# i = 1
# while len(nums) <= N:
#     if num > 9876543210:
#         break
#     if num < 10:
#         nums.append(str(num))
#     else:
#         str_num = str(num)
#         if str_num[0] > str_num[1] and str_num[1:] in nums:
#             nums.append(str_num)
#     if len(nums) == N:
#         answer = num
#     num += 1
# print(answer)