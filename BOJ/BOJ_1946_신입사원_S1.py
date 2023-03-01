import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    scores = []
    for i in range(N):
        scores.append(tuple(map(int, input().split())))

    scores.sort(reverse=True)
    print(scores)
    nums = [0]*N
    nums[0] = 1
    for i in range(1, N):
        for j in range(i-1, -1, -1):
            if scores[j][1] < scores[i][1] and nums[i] <= nums[j]:
                nums[i] = nums[j] + 1
        if nums[i] == 0:
            nums[i] = 1
    print(nums)

    answer = max(nums)
    print(answer)
    # scores.sort()
    # now = 0
    # result = 1
    # for i in range(1, N):
    #     if scores[i][1] < scores[now][1]:
    #         now = i
    #         result += 1
    # print(result)



# 1
# 9
# 9 3
# 8 1
# 7 6
# 6 7
# 5 8
# 4 2
# 3 4
# 2 9
# 1 5

# 엥 이거 반례 있는디????????????? 뭐냐???????????????