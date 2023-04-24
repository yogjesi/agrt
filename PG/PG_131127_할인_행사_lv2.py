# 23.04.25

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        arr = discount[i:i+10]
        std = True
        for item, num in zip(want, number):
            if arr.count(item) == num:
                pass
            else:
                std = False
                break
        if std:
            answer += 1

    return answer