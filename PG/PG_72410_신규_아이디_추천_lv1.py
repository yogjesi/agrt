def solution(new_id):
    # 1단계 : 소문자로 바꿈
    lower_id = new_id.lower()

    # 2단계
    cnt = 0
    while cnt < len(lower_id):
        if lower_id[cnt].isalpha() == True:
            cnt += 1
        elif lower_id[cnt].isdigit() == True:
            cnt += 1
        elif lower_id[cnt] in ['-', '_', '.']:
            cnt += 1
        else:
            lower_id = lower_id[:cnt] + lower_id[cnt+1:]
    print('2단계',lower_id)

    # 3단계 & 4단계
    now = 0
    if len(lower_id) == 1:
        if lower_id == '.':
            lower_id = ''
        else:
            pass
    else:
        while now < len(lower_id)-1:
            if now == 0 and lower_id[0] == '.':
                lower_id = lower_id[1:]
            elif lower_id[now] == '.' and lower_id[now+1] == '.':
                if now == len(lower_id)-2:
                    lower_id = lower_id[:now]
                    break
                else:
                    lower_id = lower_id[:now] + lower_id[now+1:]
            else:
                now += 1
        if len(lower_id) >= 1 and lower_id[-1] == '.':
            e = len(lower_id)-1
            lower_id = lower_id[:e]
    print('3, 4단계',lower_id)
    # 5단계
    if lower_id == '':
        lower_id = 'a'
    print('5단계', lower_id)
    # 6단계
    if len(lower_id) >= 16:
        lower_id = lower_id[:15]
        if lower_id[-1] == '.':
            end = len(lower_id)-1
            lower_id = lower_id[:end]
    print('6단계', lower_id)
    # 7단계
    if len(lower_id) <= 2:
        while len(lower_id) < 3:
            lower_id = lower_id + lower_id[-1]
    answer = lower_id
    print('answer', answer)
    return answer

# solution("...!@BaT#*..y.abcdefghijklm")
# solution("z-+.^.")
# solution("=.=")
# solution('abcdefghijklmn.p')
solution('..^')