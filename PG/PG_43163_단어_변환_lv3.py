# 23.04.08
# 이전에 풀던 코드가 있어서 일단 가져옴. 어차피 새로 풀 것임.

# DFS, BFS

from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()

    def match(word1, word2):
        same = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                same += 1
        if same == len(word1) - 1:
            return True
        else:
            return False

    def change_word():
        q.append([begin, 0])
        if target not in words:
            return 0

        while q:
            now, depth = q.popleft()
            for next_word in words:
                if match(now, next_word):
                    if next_word == target:
                        return depth + 1
                    else:
                        q.append([next_word, depth + 1])

    answer = change_word()

    return answer



# 아래는 이전 코드, 재귀 깊이 초과함
# def solution(begin, target, words):
#     answer = 0
#     l = len(begin)
#
#     def match(w1, w2):
#         cnt = 0
#         for i in range(l):
#             if w1[i] != w2[i]:
#                 cnt += 1
#         return cnt
#
#     def change_word(word, visited, cnt):
#         if word == target:
#             return cnt
#
#         if len(words) == sum(visited):
#             return 0
#
#         for i in range(len(words)):
#             if words[i] not in visited:
#                 diff = match(word, words[i])
#                 if diff == 1:
#                     visited[i] = 1
#                     change_word(words[i], visited, cnt + 1)
#                     visited[i] = 0
#
#     visited = [0] * len(words)
#     answer = change_word(begin, visited, 0)
#
#     return answer