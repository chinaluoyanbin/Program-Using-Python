"""
while True:
    try:
        h = int(input())
        s = h
        for i in range(1, 5):
            s += h
            h /= 2
        print(round(s))
        print(round(h / 2, 2))
    except:
        break
"""

# 这道题有点问题呀
while True:
    try:
        n = int(input())
        print(2.875 * n)
        print(0.03125 * n)
    except:
        break
