# 타겟 넘버

def solution(numbers, target):
    answer = 0

    def bfs(n):
        q = []
        q.append(n)
        while q:
            now = q.pop(0)
            q.append(now + numbers.)


# def solution(numbers, target):
#     answer = 0
#     leaves = [0]                       # 나 변수명 왜 이랬대...
#     for num in numbers:                # 현재 숫자는 num
#         tmp = []                       # tmp라는 임시 배열 만들고
#         for parent in leaves:          # leaves의 숫자들을 빼서
#             tmp.append(parent + num)   # num에 덧셈, 뺄셈 기호를 붙여 계산하고
#             tmp.append(parent - num)   # tmp에 넣어줌
#         leaves = tmp                   # 그리고 leaves 갱신
#     for leaf in leaves:                # 이제 모든 leaf를 꺼내서
#         if leaf == target:             # target과 일치하면 1씩 더해줌
#             answer += 1
#     return answer