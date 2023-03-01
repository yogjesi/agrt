# 3
# 40 80 60

all = int(input())
scores = list(map(int, input().split()))

highest = max(scores)
avg = 100*sum(scores)/(highest*all)
print(avg)