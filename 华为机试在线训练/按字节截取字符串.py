while True:
    try:
        s, n = input().split()
        n = int(n)
        if s[n - 1].isalpha():
            print(s[:n])
        else:
            print(s[:n + 1])
    except:
        break
