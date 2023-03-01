# 23.02.09
# lv 2


def solution(cards):
    selected = []
    num = len(cards)
    result = []
    def circle(n):
        nonlocal selected
        i = n - 1
        cnt = 1
        first = n
        selected.append(n)
        while cards[i] != first:
            selected.append(cards[i])
            i = cards[i] - 1
            cnt += 1
        return cnt

    for x in range(1, num+1):
        if x not in selected:
            inst = circle(x)
            result.append(inst)
            print(x)

    if max(result) == num:
        answer = 0
    else:
        result.sort(reverse=True)
        answer = result[0] * result[1]
    # print(answer)

    return answer

solution([8,6,3,7,2,5,1,4])
# solution([2, 1])
# solution([1, 2, 3])
