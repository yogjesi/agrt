# 197쪽

# 5
# 8 3 7 9 2
# 3
# 5 7 9

# no yes yes

# 내가 짠 코드 (반복문 사용)
def ifExist(arr, target, s, e):
    while s <= e:
        mid = (s + e)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return None


N = int(input())
now_have = list(map(int, input().split()))
now_have.sort()
M = int(input())
wanted = list(map(int, input().split()))

for part in wanted:
    if ifExist(now_have, part, 0, N-1)==None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
