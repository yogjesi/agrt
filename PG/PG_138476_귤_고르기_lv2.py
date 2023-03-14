# 23.03.14


from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    box = defaultdict(int)
    for i in tangerine:
        box[i] += 1
    result = sorted(box.items(), key=lambda x:-x[1])
    while k != 0:
        if k >= result[0][1]:
            k -= result[0][1]
            result.pop(0)
            answer += 1
            continue
        else:
            answer += 1
            break
    return answer


solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
solution(4, [1, 3, 2, 5, 4, 5, 2, 3])
solution(2, [1, 1, 1, 1, 2, 2, 2, 3])