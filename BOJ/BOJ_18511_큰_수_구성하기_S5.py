# 23.05.15

from itertools import product

N, K = map(int, input().split())
k_arr = list(map(int, input().split()))
k_arr.sort(reverse=True)     # 큰 수 부터 들어가서 비교하면 되니까 reverse로 정렬
std = ' '.join(str(N)).split()

# 앞자리 큰 수만 바꿔주면 되는 게 아닌 건가... 음...
# 물론 중복되는 경우도 있고 하니까... 근데 안 되는 경우는 없다매...
# 어쨌든 모든 경우를 세가지고 내림차순으로 정렬한 다음
# 앞자리 비교 때리고 그 다음에 바로 나오는 수를 픽하면 되는 건가?
l = len(std)
while 1:
    nums = list(product(k_arr, repeat=l))
    print(nums)
    for num in nums:
        num = list(map(str, num))
        num = int(''.join(num))
        if num <= N:
            print(num)
            exit()      # 악.... exit() 알아두기!!!!!
    l -= 1




# N, K = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)
# origin = ' '.join(str(N)).split()
# result = []
# 앞자리 단위만 맞추면 나머지 밑에는 뭐... 걍... 맘대로...
# std = False
# for num in origin:
#     if (result and result[0] < origin[0]) or std:
#         result.append(str(arr[0]))
#         continue
#     std = False
#     for i in arr:
#         if int(num) > i:
#             result.append(str(i))
#             std = True
#             break
#         if int(num) == i:
#             result.append(str(i))
#             break
# answer = ''.join(result)
# print(answer)
