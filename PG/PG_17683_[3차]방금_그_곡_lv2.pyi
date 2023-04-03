# 23.04.01

# import datetime
#
# def solution(m, musicinfos):
#     answer = '(None)'
#     stack = []
#     stack.extend(m)
#     cnt = 0
#     while cnt < len(stack):
#         if stack[cnt] == '#':
#             stack[cnt - 1] = stack[cnt - 1] + '#'
#             stack.pop(cnt)
#         else:
#             cnt += 1
#
#     for music in musicinfos:
#         start, end, name, melody = music.split(',')
#         st = datetime.datetime.strptime(start, '%H:%M')
#         et = datetime.datetime.strptime(end, '%H:%M')
#         time = (et - st).seconds // 60
#         runtime = len(melody)
#         last = melody * (time // runtime + 1)
#         last = last[:time]
#         result = []
#         for i in range(len(last)):
#             if last[i] == '#':
#                 result[-1] = result[-1] + '#'
#             else:
#                 result.append(last[i])
#         for x in range(len(result) - len(stack)):
#             if stack == result[x:x + len(stack)]:
#                 return name
#     return answer

# import datetime
#
#
# def solution(m, musicinfos):
#     answer = ["(None)", 0]
#     stack = []
#     stack.extend(m)
#     cnt = 0
#     while cnt < len(stack):
#         if stack[cnt] == '#':
#             stack[cnt - 1] = stack[cnt - 1] + '#'
#             stack.pop(cnt)
#         else:
#             cnt += 1
#
#     for music in musicinfos:
#         start, end, name, melody = music.split(',')
#         st = datetime.datetime.strptime(start, '%H:%M')
#         et = datetime.datetime.strptime(end, '%H:%M')
#         time = (et - st).seconds // 60
#         runtime = len(melody)
#         last = melody * (time // runtime + 1)
#         last = last[:time]
#         result = []
#
#         for i in range(len(last)):
#             if last[i] == '#':
#                 result[-1] = result[-1] + '#'
#             else:
#                 result.append(last[i])
#
#         for x in range(len(result) - len(stack) + 1):
#             if stack == result[x:x + len(stack)]:
#                 if answer[1] < time:
#                     answer = [name, time]
#
#     return answer[0]

