# 2022.08.04
# 백준
# 그리디

N = int(input())

# left_sugar : 5kg짜리에 다 담고 남은 설탕의 양
# five_kg_cnt : 5kg 짜리 봉지 갯수
# result : 결과값 담을 곳, default는 -1
left_sugar = N%5
five_kg_cnt = N//5
result = -1

# five_kg_cnt가 0이 될 때까지
while five_kg_cnt >= 0:
    if left_sugar == 0:                #..............만약 5kg 짜리 봉지에 다 담고 남은 설탕의 양이 0이면
        result = five_kg_cnt           #..............5kg 봉지에만 담으면 되므로 바로 result로 반환하고 break
        break
    elif left_sugar >= 3 and left_sugar % 3 == 0: #...만약 남은 설탕량이 3kg 이상이면서 3kg짜리 봉지에 딱맞게 나눠담아질 때
        three_kg_cnt = left_sugar // 3 #..............3kg짜리 봉지에 나눠담으면 몇 봉지가 나오는지 세고
        result = five_kg_cnt + three_kg_cnt   #.......5kg짜리 봉지 갯수 + 3kg짜리 봉지 갯수 합해서 result로 반환, break
        break
    else:                             #...............위의 두 케이스가 아니면 딱 떨어지게 나뉘지 않는다는 뜻이니까
        five_kg_cnt -= 1              #...............5kg짜리 봉지 하나 까고
        left_sugar += 5               #...............남은 설탕에 5kg 추가해주자

print(result)