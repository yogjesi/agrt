# 이전에 풀었던 방법

# def solution(phone_book):
#     # 앞번호로 분류하자
#     initial = {'0':[],}
#     for j in range(1, 10):
#         initial[str(j)] = []
#     re_phone_book = sorted(phone_book)
#     answer = True
#     for idx in range(len(re_phone_book)):
#         a = re_phone_book[idx][0]
#         for num_len in range(1, len(re_phone_book[idx])):
#             if re_phone_book[idx][:num_len] in initial[a]:
#                 answer = False
#         initial[a].append(re_phone_book[idx])
#         if answer == False:    # 있으면 for문 바로 나오라고
#             break
#     print(initial)
#     return answer

# 23.03.20
def solution(phone_book):
    answer = True
    # phone_book = sorted(phone_book)
    ini = {}
    for num in phone_book:
        ini[num] = 1
    for phone_num in phone_book:
        pre = ""
        for num in phone_num:
            pre += num
            if pre in ini and pre != phone_num:
                return False
    return answer

solution(["1195524421", "119", "97674223"])