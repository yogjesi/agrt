# 23.03.31

from collections import defaultdict

def solution(n, words):
    answer = [0, 0]
    play = defaultdict(list)
    for i in range(1, n + 1):
        play[i] = []

    stack = []
    for num, word in enumerate(words):
        num += 1

        if num % n == 0:
            play[n].append(word)
        else:
            play[num % n].append(word)

        if word in stack or (stack != [] and stack[-1][-1] != word[0]):
            if num % n == 0:
                answer[1] = play[n].index(word) + 1
                answer[0] = n
                return answer
            else:
                answer[1] = play[num % n].index(word) + 1
                answer[0] = num % n
                return answer
        stack.append(word)

    return answer