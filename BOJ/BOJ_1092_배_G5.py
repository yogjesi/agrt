# 23.05.03

# N은 50보다 작거나 같은 자연수
import sys

N = int(input())
# 각 컨테이너의 적재 제한
cranes = list(map(int, input().split()))
M = int(input())
# 옮겨야 할 박스들의 무게
boxes = list(map(int, input().split()))
# 정렬
cranes.sort(reverse=True)
boxes.sort(reverse=True)

# 만약 박스 무게가 제일 큰 크레인 허용범위를 넘어선다면
for box in boxes:
    if box > cranes[0]:
        print(-1)
        sys.exit()

cnt = 0
while len(boxes)>0:
    for crane in cranes:
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    cnt += 1
print(cnt)

# 본격적으로 적재
# visited = [0] * M
# cnt = 0
# while True:
#     for crane in cranes:
#         for i, box in enumerate(boxes):
#             if crane >= box and visited[i]==0:
#                 visited[i] = 1
#                 break
#     cnt += 1
#     if sum(visited) == M:
#         break
# print(cnt)




# for item in weight:
#     if item > limit[0]:
#         cnt = -1
#         break
#
# if cnt == -1:
#     print(cnt)
# else:
#     while sum(visited)<M:
#         for i in range(len(limit)):
#             for j in range(len(weight)):
#                 if limit[i] >= weight[j] and visited[j] == 0:
#                     visited[j] = 1
#                     break
#         cnt += 1
#     print(cnt)