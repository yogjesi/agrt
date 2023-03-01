# 방법 1 : 런타임 에러 오지게 남

# import collections
#
# def solution(N, stages):
#     cd = collections.defaultdict(int)
#     for num in range(1, N + 2):
#         cd[num] = 0
#     challenger = [0] * (N + 2)
#     for i in stages:
#         cd[i] += 1
#         for j in range(1, i + 1):
#             challenger[j] += 1
#
#     nc = [0] * (N + 1)
#
#     for n in range(1, N + 1):
#         nc[n] = (cd[n] / challenger[n], n)
#     nc.pop(0)
#     result = sorted(nc, key=lambda x: (-x[0], x[1]))
#     answer = []
#     for m in range(len(result)):
#         answer.append(result[m][1])
#     print(answer)
#     return answer



# 방법 2 : 1보다 실패가 뜸... 애초에 어딘가 틀린 듯

# def solution(N, stages):
#     answer = []
#     stg = [0]*(N+2)
#     for i in stages:
#         stg[i] += 1
#     clear = stg[:]   # deep copy
#     for i in range(1, N+2):
#         clear[i] = clear[i] + clear[i-1]
#     clear.insert(0, 0)
#     clear.pop()
#     for i in range(1, N+2):
#         clear[i] = 8-clear[i]
#     nc = []
#     for n in range(1, N+1):
#         nc.append((stg[n]/clear[n], n))
#     result = sorted(nc, key=lambda x: (-x[0], x[1]))
#     for i in range(len(result)):
#         answer.append(result[i][1])
#     # print(answer)
#     return answer


# 3번째도 실패

def solution(N, stages):
    p = len(stages)
    clg = {}
    for i in range(1, N + 2):
        clg[i] = 0
    stg = [0] * (N + 2)

    # clg(challenger) 수 담기
    for lv in stages:
        clg[lv] += 1

    base = [p] * (N + 2)
    for n in range(1, N + 2):
        if n == 1:
            stg[n] = clg[n]
        else:
            stg[n] = stg[n - 1] + clg[n]
        base[n] -= stg[n]
    for m in range(1, N + 1):
        clg[m] = clg[m] / base[m - 1]
    clg.pop(N + 1)
    result = sorted(clg, key=lambda x: -clg[x])

    return result


# 통과 : 이유는 : stage 끝에 아무도 도달하지 못했을 때의 케이스를 넣어줘야... 안그럼 0을 나누게 되서 런타임 에러 뜬다고.
def solution(N, stages):
    answer = []
    p = len(stages)
    clg = {}
    for i in range(1, N + 2):
        clg[i] = 0
    # clg(challenger) 수 담기
    for lv in stages:
        clg[lv] += 1

    # stg 통과 인원 수 만들기
    stg = [0] * (N + 2)
    base = [0] * (N + 2)
    for j in range(1, N + 1):
        stg[j] = clg[j] + stg[j - 1]
        base[j] = p - stg[j - 1]
        if base[j] != 0:
            clg[j] = clg[j] / base[j]
        else:
            clg[j] = 0

    clg.pop(N + 1)
    answer = sorted(clg, key=lambda x: -clg[x])
    print(answer)

    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) # [3, 4, 2, 1, 5]