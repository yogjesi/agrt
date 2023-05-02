# 23.05.01

from heapq import heappush, heappop, heapify

N = int(input())
meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))
meetings.sort(key=lambda x:x[0])

cnt = 1
pre_step = [0]

for s, e in meetings:
    if pre_step[0] <= s:  # 회의를 이어갈 수 있으면
        heappop(pre_step)  #
    else:   # 회의를 못 이어가면
        cnt += 1  #강의실 추가
    heappush(pre_step, e)
print(cnt)


# while meetings:
#     ns, ne = heappop(meetings)
#     for i in range(len(pre_step)):
#         if pre_step[i] <= ns:
#             pre_step[i] = ne
#             break
#         if i == len(pre_step)-1:
#             pre_step.append(ne)
# answer = len(pre_step)
# print(answer)
