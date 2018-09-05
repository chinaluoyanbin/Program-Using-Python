def is_ascending(lyst):
    flag = True
    for i in range(len(lyst) - 1):
        if lyst[i] >= lyst[i + 1]:
            flag = False
    return flag


while True:
    try:
        n = int(raw_input())
        a = list(map(int, raw_input().split()))
        left = -1
        right = -1
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                left = i
                break
        for i in range(left + 1, n - 1):
            if a[i] < a[i + 1]:
                right = i
                break
        if left == -1:
            print('no')
        else:
            if right == -1:
                res = a[:left] + list(reversed(a[left:]))
                if is_ascending(res):
                    print('yes')
                else:
                    print('no')
            else:
                res = a[:left] + list(reversed(
                    a[left:right + 1])) + a[right + 1:]
                if is_ascending(res):
                    print('yes')
                else:
                    print('no')
    except:
        break
"""
4
2 1 3 4
"""
