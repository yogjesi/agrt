# 23.05.08
# 똑바로 가면 안 되는군...
def solution(numbers):
    answer = [-1]*len(numbers)
    # for i in range(len(numbers)-1):
    #     for j in range(i+1, len(numbers)):
    #         if numbers[j] > numbers[i]:
    #             answer[i] = numbers[j]
    #             break
    for i in range(len(numbers)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if numbers[j] < numbers[i]:
                answer[j] = numbers[i]
            else:
                break
    return answer