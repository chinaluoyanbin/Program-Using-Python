while True:
    try:
        n = int(input())
        count = 1
        res = []
        for i in range(n):
            res.append([])
            j = i
            while j >= 0:
                res[j].append(str(count))
                count += 1
                j -= 1
        for i in range(n):
            print(' '.join(res[i]))
    except:
        break
