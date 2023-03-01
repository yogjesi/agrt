# 보니까 저번에 풀던 것 같긴 한데 언제 풀었는지 기억은 안남
# 완수는 못했으니 이번에 새로운 마음으로 다시 해보는 걸로....
# 23.02.10
# lv 2

def solution(name):
    answer = 0
    word = {}
    for apb in range(65, 91):
        word[chr(apb)] = apb - 65
    cn = []
    for n in name:
        inst = min(word[n],26-word[n])
        cn.append(inst)

    min_dist = len(name) - 1
    if cn[1] == 0 and cn[-1] == 0:
        if sum(cn) == 0:
            min_dist = 0
        else:
            cnt_a = 0
            cnt_b = 0
            for i in range(1, len(cn)):
                if cn[i] == 0:
                    cnt_a += 1
                else:
                    break
            for j in range(len(cn)-1, 0, -1):
                if cn[j] == 0:
                    cnt_b += 1
                else:
                    break
            inst = max(cnt_a, cnt_b)
            min_dist -= inst
    elif cn[1] == 0:
        cnt = 0
        for i in range(1, len(cn)):
            if cn[i] == 0:
                cnt += 1
            else:
                break
        min_dist -= cnt
    elif cn[-1] == 0:
        cnt = 0
        for j in range(len(cn)-1, 0, -1):
            if cn[j] == 0:
                cnt += 1
            else:
                break
        min_dist -= cnt
    answer = sum(cn) + min_dist
    print(answer)
    return answer


solution("AAAACAA") # 5
solution("AAAAAA") # 0
solution("JAN")


# 아래는 옛날 코드
# def solution(name):
#     dict_alp = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,
#                 "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14,
#                 "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
#                 "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
#     l = len(name)
#     default = ["A"] * l
#     answer = 0
#     for i in range(l):
#         t = name[i]
#         gap = abs(dict_alp[t] - 1)
#         if gap > 13:
#             gap = abs(26 - gap)
#             answer += gap
#         else:
#             answer += gap
#
#     cnt = 0
#     for i in range(l):
#         x = name.find("A" * i)
#         if x > cnt:
#             cnt = x
#
#     answer += l - 1 - cnt
#
#     return answer