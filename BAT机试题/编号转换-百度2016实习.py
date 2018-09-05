import re


Letters = [chr(65 + i) for i in range(0, 26)]


def RxCy2AAdd(s):
    x, y = s[1:].split('C')
    y = int(y)
    AA = ''
    if y == 26:
        AA += 'Z'
    else:
        while y > 0:
            AA = Letters[y % 26 - 1] + AA
            y //= 26
    return AA + x


def AAdd2RxCy(s):
    AA, dd = list(re.search('[A-Z]+', s).group(0)), re.search('[0-9]+', s).group(0)
    AA.reverse()
    y = 0
    for i, el in enumerate(AA):
        y += 26 ** i *(Letters.index(el) + 1)
    return 'R' + dd + 'C' + str(y)


def solution(targets):
    res = []
    for el in targets:
        if re.match('^[A-Z]\d+[A-Z]\d+$', el):
            res.append(RxCy2AAdd(el))
        else:
            res.append(AAdd2RxCy(el))
    return res


while True:
    try:
        T = int(raw_input())
        targets = []
        for i in range(T):
            targets.append(raw_input())
        res = solution(targets)
        for el in res:
            print(el)
    except:
        break

"""
2
R23C55
BC23
"""
"""
BC23
R23C55
"""
