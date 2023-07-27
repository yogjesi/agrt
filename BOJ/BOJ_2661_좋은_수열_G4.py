# 23.07.15
import sys

N = int(input())
## 123212
def check(arr):
    arr_len = len(arr)
    for part_len in range(1, arr_len//2 + 1):
        for part_start in range(part_len, arr_len - part_len + 1):
            if arr[part_start-part_len:part_start] == arr[part_start:part_start+part_len]:
                return False
    else:
        return True

def dfs(arr, depth):
    if depth == N:
        print("".join(list(map(str, arr))))
        sys.exit() # 최단만 구하면 되니까

    arr.append(1)
    for i in range(1, 4):  # 왜냐하면 1부터 3까지 숫자가 들어갈 수 있어서
        arr.pop()
        arr.append(i)
        if check(arr):
            if not dfs(arr, depth+1):
                continue
    else: # for else 구문 넘나 오랜만... 순간 헷갈렸네
        arr.pop()
        return False

dfs([1], 1)

# 1 good
# 11 bad
# 12 good
# 121 good
# 1211 bad
# 1212 bad
# 1213 good
# 12131