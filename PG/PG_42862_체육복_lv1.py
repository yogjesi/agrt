# 23.04.25
# 풀려있군...
# 언젠지도 모르겠넹...

def solution(n, lost, reserve):
    students = [1] * (n + 1)

    for i in range(1, n + 1):
        if i in reserve:
            students[i] += 1  # 여벌이 있는 친구
        if i in lost:
            students[i] -= 1  # 하나만 도난당함
    print(students)

    for j in lost:
        if j in reserve:
            reserve.remove(j)
    print(reserve)

    for k in range(1, n + 1):
        if students[k] == 0:
            if k - 1 in reserve:
                students[k] = 1
                reserve.remove(k - 1)
            elif k + 1 in reserve:
                students[k] = 1
                reserve.remove(k + 1)

    for num in range(1, n + 1):
        if students[num] != 0:
            students[num] = 1
    answer = sum(students) - 1

    return answer