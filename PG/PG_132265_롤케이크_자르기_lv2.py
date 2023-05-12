# 23.05.12
# 그냥... 딕셔너리...?

from collections import defaultdict

# 관건은 주어지는 topping의 길이가 1,000,000이므로
# for문 중첩시키면 시간 초과 발생
# 따라서 한 번 탐색할 때 전부 해결할 수 있도록 하면 좋겠군
def solution(topping):
    answer = 0
    front = set([])                 # 왼쪽 : set으로 잡아서 갯수만 보게
    back = set(topping)             # 오른쪽 : 역시 set으로 잡기
    nums = defaultdict(int)         # nums : 각 토핑의 개수 담는 딕셔너리
    # defaultdic 채우기
    for top in topping:
        nums[top] += 1
    # 한 번 돌 때 전부 처리
    for i in range(len(topping)):
        front.add(topping[i])       # 토핑을 앞쪽에 넣고
        nums[topping[i]] -= 1       # 해당 토핑 개수 줄이기
        if nums[topping[i]] == 0:   # 만약 nums에 이 토핑이 하나도 없으면
            back.remove(topping[i]) # back에서 이 토핑 없애주기
        if len(front) == len(back): # front와 back 토핑 개수 같으면
            answer += 1             # answer에 반영

    return answer