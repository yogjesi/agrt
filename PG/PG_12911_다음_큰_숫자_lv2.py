# 23.03.07

# def solution(n):
#     bnum = format(n, 'b')
#     cnum = str(bnum)
#     l = len(cnum)
#     result = []
#     result.extend(cnum)
#     if result.count('0') == 0:
#         result.insert(0, '1')
#         result[1] = '0'
#     else:
#         for i in range(l - 2, -1, -1):
#             if result[i + 1] == '1' and result[i] == '0':
#                 result[i + 1] = '0'
#                 result[i] = '1'
#                 break
#
#     preans = '0b' + ''.join(result)
#     answer = int(preans, 2)
#     print(answer)
#
#     return answer


def solution(n):
    answer = 0
    result = []
    bnum = format(n, 'b')

    for i in range(1, 1000000):
        inst = n
        inst += i
        new = format(inst, 'b')
        if bnum.count('1') == new.count('1'):
            break
    res = '0b' + new
    # print(res)
    answer = int(res, 2)
    return answer