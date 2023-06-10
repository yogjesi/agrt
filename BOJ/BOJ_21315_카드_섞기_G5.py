# 23.06.10
# 카드섞기
# 완전 탐색...이라는데 완탐?????? 적어도 난 그렇게 안 푼 듯.

# 1. 입력부
N = int(input())
nums = list(map(int, input().split()))

# 2. 첫 번째 K 구하기 : 카드 섞을 때마다 맨 끝의 숫자가 앞에 오는 것을 이용함
first_end = N - nums[0]
for i in range(1, 10):              # 어차피 2^10은 1024이므로 범위를 넘어감
    if 2**i == first_end:
        k1 = i                      # k1 : 첫 번째 K
        break

# 3. 두 번째 K 구하기
for idx, num in enumerate(nums):    # 3-1. N의 인덱스 값 구하기 (맨 앞에 있던 N이 얼마나 밀렸는가?)
    if num == N:
        second_end = idx
        break
for j in range(1, 10):              # 3-2. 첫 번째 K 구하는 것과 동일한 방식
    if 2**j == second_end:
        k2 = j
        break

# 4. 출력부
print(f"{k1} {k2}")


