while True:
    try:
        s = input()
        res = []
        while s:
            index = s.index(max(s))
            res.append(s[index])
            s = s[index + 1:]
        print(''.join(res))
    except:
        break
