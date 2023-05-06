# 23.05.06
# DP라는데 난 아직 DP에 숙달되진 않은 듯
# 그래도 이건 아는 문제 ㅋㅋ
# ...는 인덱스 주의, 그리고 문제 끝까지 잘 읽어야 할 듯. 으악.
# 나누기하고 나머지로 구하는 부분 안해서 실패함...

def solution(m, n, puddles):
    field = [[0]*(m+1) for _ in range(n+1)]
    field[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            if [j, i] in puddles:
                field[i][j] = 0
                continue
            num = (field[i-1][j] + field[i][j-1]) % 1000000007
            field[i][j] = num
    answer = field[-1][-1]
    return answer