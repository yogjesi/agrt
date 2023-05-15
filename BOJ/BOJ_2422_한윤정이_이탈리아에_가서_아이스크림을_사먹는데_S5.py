# 23.05.15
# 문제 이름 왤케 기냐

# 맛없는 조합은 피하고 싶은 윤정이
# 선택하는 방법 몇 가지?
# 제한 : 아이스크림 종류는 200가지 이하
# 섞어먹으면 안 되는 조합 개수는 10,000가지 이하

N, M = map(int, input().split())

bad = []
for _ in range(M):
    a, b = map(int, input().split())
    bad.append((a, b))
print(bad)