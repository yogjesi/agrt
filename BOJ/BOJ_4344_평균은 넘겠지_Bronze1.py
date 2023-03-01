# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

T = int(input())

for t in range(T):
    nums = list(map(int, input().split()))
    num = nums.pop(0)
    avg = sum(nums)/num
    cnt = 0
    for i in range(num):
        if nums[i] > avg:   # 넘는다는 건 이상인지? 초과인지? 표현이 애매하네.
            cnt += 1
    ans = 100*cnt/num
    print('{:.3f}%'.format(ans))
