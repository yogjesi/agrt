# 23.03.08
# 23.04.04

import heapq

def solution(operations):
    answer = [0, 0]
    hq = []
    # hq_max = []
    for odrs in operations:
        odr, num = odrs.split()
        n = int(num)
        if odr == "I":           # insert
            heapq.heappush(hq, n)
            # heapq.heappush(hq_max, (-num, num))
        elif odr == "D":    # delete
            if len(hq) == 0:
                continue
            if n == 1:  # delete maximal value
                hq = heapq.nlargest(len(hq), hq)[1:]
                heapq.heapify(hq)
                # heapq.heappop(hq_max)
            if n == -1:
                heapq.heappop(hq)
    answer[0] = max(hq)
    answer[1] = hq[0]
    print(answer)

    return answer

solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])