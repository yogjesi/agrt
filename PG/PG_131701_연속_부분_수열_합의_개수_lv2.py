# 23.05.05
# so easy!

def solution(elements):
    arr = set([])
    arr.update(elements)
    new_e = elements*2
    for i in range(2, len(elements)+1):
        for j in range(len(elements)):
            subs = new_e[j:j+i]
            num = sum(subs)
            arr.add(num)
    answer = len(arr)
    return answer