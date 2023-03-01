# 상근이는 2863번에서 표를 너무 열심히 돌린 나머지 5와 6을 헷갈리기 시작했다.

# 상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고,
# 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.

# 두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다.
# 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.


A, B = input().split()

max_a = []
min_a = []
max_b = []
min_b = []

max_a.extend(A)
min_a.extend(A)
max_b.extend(B)
min_b.extend(B)

for i in range(len(A)):
    if A[i] == '6':
        min_a[i] = '5'
    if A[i] == '5':
        max_a[i] = '6'

for j in range(len(B)):
    if B[j] == '6':
        min_b[j] = '5'
    if B[j] == '5':
        max_b[j] = '6'

max_a = ''.join(max_a)
max_b = ''.join(max_b)
min_a = ''.join(min_a)
min_b = ''.join(min_b)

max_num = int(max_a) + int(max_b)
min_num = int(min_a) + int(min_b)

print(min_num, max_num)