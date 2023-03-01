# medium
# 23.02.05
# decode ways

class Solution:
    def numDecodings(self, s: str) -> int:
        case = [0] * len(s)

        for idx in range(len(s)):
            if idx == 0:
                if s[idx] != "0":
                    case[idx] = 1
                    continue
                else:  # 불가능한 경우임
                    return 0

            if int(s[idx - 1:idx + 1]) >= 10 and int(s[idx - 1:idx + 1]) <= 26:  # 1에서 26 사이일 때
                if int(s[idx]) != 0:  # 0이 아닐 때
                    case[idx] = case[idx - 1] + 1
                else:  # 0일 때
                    if int(s[idx - 1]) >= 3:  # 만일 10자리가 3이상이면 어차피 불가능하므로
                        return 0
                    elif int(s[idx - 1]) <= 2 and int(s[idx - 1]) > 0:  # 10자리가 가능한 수라면
                        if idx >= 2 and case[idx - 2] < case[idx - 1]:  # 이전 숫자에 영향을 받는 경우
                            case[idx] = case[idx - 1] - 1
                            case[idx - 1] = case[idx]
                        else:  # 이전 숫자가 없는 경우
                            case[idx] = case[idx - 1]
                    elif int(s[idx - 1]) == 0:  # 0이 두 번 연속으로 오면 불가능하다
                        return 0
            else:  # 만든 조합이 1에서 26 사이가 아닐 때
                if int(s[idx]) != 0:
                    case[idx] = case[idx - 1]
                else:
                    return 0
            print(case)
        return case[-1]
#
#
#
#     numDecodings("226")

class Solution(object):
    def numDecodings(self, s):
        if s == '':
            return 0
        first = (0, 0)      # (현재 숫자 = cur_num, 만들 수 있는 갯수 = can_make)
        if int(s[0]) != 0:
            second = (0, 1)
        else:
            second = (0, 0)

        can_make = 0     # 만들 수 있는 갯수

        for i in range(len(s)):
            cur_num = int(s[i])                   # 현재 숫자
            if second[0] == 1 or (second[0] == 2 and cur_num < 7):  # 10~26일 때
                if cur_num != 0:
                    can_make = first[1] + second[1]
                else:
                    can_make = first[1]
            else:
                if cur_num != 0:
                    can_make = second[1]
                else:
                    can_make = 0
            first = second
            second = (cur_num, can_make)

        return second[1]
