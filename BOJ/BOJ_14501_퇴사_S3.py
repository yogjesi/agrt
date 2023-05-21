# 23.05.21

N = int(input())

# T : the day which is possible to do service
# P : the payment that he can get on the day
arr = [(0, 0)]                      # (T, P)값 누적용, 추후에 인덱스로 돌릴 거라서 (0, 0)을 미리 넣어두었음.
for _ in range(N):
    T, P = map(int, input().split())
    arr.append((T, P))
result = [0]*(N+1)                  # result = N일 내 최대 페이 누적용 배열, result[i]일 때 i일 까지 일했을 때 벌 수 있는 최대 페이값을 넣을 거임
                                    # 인덱스와 N을 일치시키기 위해 배열의 길이를 N+1로 두고 0번은 사용하지 않음
for i in range(1, N+1):             # 1 ~ N일동안 돌면서
    t, p = arr[i]                   # i일의 t, p 값을 뽑아내고
    if i + t - 1 > N:               # (i + t - 1)일까지 일을 해야 하는데 이게 마지막 근무일인 N보다 크면 나가리
        continue
    if p + max(result[:i]) > result[i+t-1]:         # 만약 이전까지의 최대 페이 + 현재 얻을 수 있는 페이 값이 이전에 누적된 페이보다 크다면
        result[i+t-1] = p + max(result[:i])         # 새롭게 값을 갈아치워준다.
print(max(result))                                  # 그리고 result에서 최대값 뽑아주면 끝.