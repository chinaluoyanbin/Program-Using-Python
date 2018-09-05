def solution(s, t):
    s = list(s)
    t = list(t)
    t.sort(reverse=True)
    index = 0
    for i in range(len(s)):
        if s[i] < t[index]:
            s[i] = t[index]
            index += 1
        if index == len(t):
            break
    return ''.join(s)

while True:
    try:
        s = input()
        t = input()
        print(solution(s, t))
    except:
        break
