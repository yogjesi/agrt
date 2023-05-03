def solution(files):
    answer = []
    result = []
    # 각 파일명을 head, number으로 구분하기
    for idx, file in enumerate(files):
        now = []
        for i, s in enumerate(file):
            if file[i].isdigit():
                now.append(file[:i].lower())   # head의 lowercase
                ns = i
            if not file[i].isdigit() and file[i-1].isdigit():
                now.append(int(file[ns:i]))    # num, 정렬 편하라고 숫자 처리
                break
        now.append(idx)                # 기존 배열 인덱스
        result.append(now)
    return answer


# runtime Error :  아무래도 정렬 방법을 다른 걸로 써야 하나 싶다...
def solution(files):
    answer = []
    nums = ["0", "1", "2", "3", "4",
            "5", "6", "7", "8", "9"]
    result = []
    # 각 파일명을 head, number으로 구분하기
    for idx, file in enumerate(files):
        now = []
        for i, s in enumerate(file):
            if s in nums and file[i-1] not in nums:
                now.append(file[:i].lower())   # head의 lowercase
                # head = file[:i]
                ns = i
            if s not in nums and file[i-1] in nums:
                now.append(int(file[ns:i]))    # num, 정렬 편하라고 숫자 처리
                # num = file[ns:i]
                # tail = file[i:]
                break
        now.append(idx)                # 기존 배열 인덱스
        # now = [head, num, tail]
        result.append(now)
    # result.sort(key=lambda x: (x[0].lower(), int(x[1])))
    result.sort()
    print(result)
    for a, b, i in result:
        answer.append(files[i])
    # answer = [''.join(name) for name in result]
    return answer