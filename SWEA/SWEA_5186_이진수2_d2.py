# 23.04.27

# 소숫점 이진수 문제
T = int(input())

for tc in range(1, T+1):
    N = float(input())
    answer = []
    for i in range(1, 13):
        if N == 0.0:
            break
        num = N // 2**(-i)
        if num == 0:
            answer.append("0")
        else:
            answer.append("1")
            N -= num*(2**(-i))

    if N > 0:
        answer = "overflow"
    else:
        answer = "".join(answer)

    print(f"#{tc} {answer}")
