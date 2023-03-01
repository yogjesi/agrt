# 22.09.09

# 매일 카카오 한 문제 풀기

# sum을 너무 많이 써도 안됨
# deque 써서 속도 좀 빠르게 해주는 것도 필요함


from collections import deque

def solution(queue1, queue2):
    # max_num을 *3으로 잡아주는 이유 :
    max_num = len(queue1)*3
    q1 = deque(queue1)
    q2 = deque(queue2)
    log_q1 = sum(queue1)
    log_q2 = sum(queue2)

    cnt = 0
    answer = -1

    # while문 한 번 돌면 작업 1회 수행
    while (queue1 and queue2) and cnt < max_num:
        if log_q1 == log_q2:
            return cnt
        elif log_q1 > log_q2:
            q2.append(q1.popleft())
            log_q2 += q2[-1]
            log_q1 -= q2[-1]
        elif log_q1 < log_q2:
            q1.append(q2.popleft())
            log_q1 += q1[-1]
            log_q2 -= q1[-1]
        cnt += 1
    return answer

result = solution([1, 2, 1, 2], [1, 10, 1, 2])
print(result)