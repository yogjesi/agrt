# 23.03.03

# 예전에 시도했었나봄
# def solution(s):
#     sentence = s.lower()
#     words = list(sentence.split())
#     print(words)
#     new_sent = []
#     for i in range(len(words)):
#         words[i][0].replace(words[i][0].upper())
#     answer = ' '.join(words)
#     return answer

# 지금

# def solution(s):
#     sentence = s.lower()
#     words = list(sentence.split())
#     result = []
#     for word in words:
#         nw = word[0].upper() + word[1:]
#         result.append(nw)
#     answer = ' '.join(result)
#     return answer


def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0 and s[i] != ' ':
            answer = answer + s[i].upper()
        elif s[i-1] == ' ' and s[i] != ' ':
            answer = answer + s[i].upper()
        else:
            answer = answer + s[i].lower()
    print(answer)
    return answer


solution(" 3people unFollowed   me")