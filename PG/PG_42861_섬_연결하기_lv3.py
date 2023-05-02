# 23.04.28
# greedy라는데...

# 크루스칼 Kruskal
# 근데 왜 유니온 파인드여... 왜 일반 리스트론 체크가 안되는 걸까...
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    # print(costs)
    # check = [False]*n
    link = set([costs[0][0]])   # I wonder this part
    print(link)
    while len(link) != n:
        for v in costs:
            if v[0] in link and v[1] in link:
                continue
            if v[0] in link or v[1] in link:
                link.update([v[0], v[1]])
                answer += v[2]
                print(answer, link)
                break
    # for i, j, cost in costs:
    #     if check[i] and check[j]:
    #         continue
    #     check[i], check[j] = True, True
    #     answer += cost

    return answer



# 아래도 시간초과 및 실패
# from itertools import combinations, permutations
# def solution(n, costs):
#     answer = 0
#     # 순열 만듦
#     nums = [i for i in range(n)]
#     permu = list(permutations(nums, n))
#     # 비용점수판 만듦
#     check = [[0] * n for _ in range(n)]
#     for i, j, cost in costs:
#         check[i][j] = cost
#         check[j][i] = cost
#     # print(check)
#     result = float('inf')
#     # 만들어진 순열 따라서 점수 계산
#     for case in permu:
#         cnt = 0
#         for k in range(1, n):
#             r, c = case[k - 1], case[k]
#             if check[r][c] == 0 or cnt >= result:
#                 break
#             else:
#                 cnt += check[r][c]
#             if k == n - 1:
#                 if result > cnt:
#                     result = cnt
#     answer = result
#
#     return answer


# 아래는 1차 시도, 2개 맞고 시간초과나 실패 뜸
# def solution(n, costs):
#     answer = 0
#     check = [[0] * n for _ in range(n)]
#     for i, j, cost in costs:
#         check[i][j] = cost
#         check[j][i] = cost
#     result = []
#
#     def dfs(r, cnt, visited):
#         nonlocal result
#         if len(visited) == n:
#             result.append(cnt)
#             return
#
#         for c in range(n):
#             this_cost = check[r][c]
#             # print('this cost:', this_cost)
#             if c not in visited and this_cost != 0:
#                 visited.append(c)
#                 # print('visited 1', visited)
#                 dfs(c, (cnt + this_cost), visited)
#                 visited.remove(c)
#                 # print('visited 2', visited)
#
#     for k in range(n):
#         visited = [k]
#         dfs(k, 0, visited)
#     # print(result)
#     answer = min(result)
#     return answer