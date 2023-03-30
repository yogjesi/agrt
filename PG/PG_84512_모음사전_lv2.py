# 23.03.30

def solution(word):
    answer = 0
    words = "AEIOU"
    word_list = []

    def all(cnt, w):
        if cnt == 5:
            return
        for n in words:
            word_list.append(w + n)
            all(cnt + 1, w + n)
    all(0, "")
    answer = word_list.index(word) + 1
    print(answer)
    return answer

solution("EIO")