# 23.03.30

def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            num = 0
            for j in range(len(arr2)):
                num += arr1[i][j]*arr2[j][k]
            answer[i][k] = num
    return answer