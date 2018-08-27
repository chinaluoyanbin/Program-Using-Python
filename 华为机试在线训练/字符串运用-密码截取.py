while True:
    try:
        s = input()
        maxLen = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                maxLen = 2
                x = 1
                while i - x >= 0 and i + 1 + x < len(s) and s[i - x] == s[i + 1 + x]:
                    if maxLen < 2 * (x + 1):
                        maxLen = 2 * (x + 1)
                    x += 1
            if i > 0 and s[i - 1] == s[i + 1]:
                y = 1
                while i - y >= 0 and i + y < len(s) and s[i - y] == s[i + y]:
                    if maxLen < 2 * y + 1:
                        maxLen = 2 * y + 1
                    y += 1
        print(maxLen)
    except:
        break
