# 23.05.18

# 아놔 내일 걸 먼저 풀어버림... 이게 오늘(18일) 거...
# ...왜 실버4? 더 쉬울 거 같은데 (10분 컷)

from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]  # 나중에 조합하기 쉽게 '문자'로 받을 거임

pairs = list(permutations(cards, k))
result = set([])                     # 중복을 피하기 위한 set 설정
for nums in pairs:
    num = ''.join(nums)              # 하나의 문자열로 합쳐서 result에 넣어버리면 끝
    result.add(num)
print(len(result))