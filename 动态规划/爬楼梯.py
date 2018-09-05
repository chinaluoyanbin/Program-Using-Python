def climb_stairs(m):
    if m == 1:
        return 1
    elif m == 2:
        return 1
    else:
        return climb_stairs(m - 1) + climb_stairs(m - 2)


while True:
    try:
        n = int(raw_input())
        for i in range(n):
            m = int(raw_input())
            if m == 1:
                print('0')
            else:
                print(climb_stairs(m))
    except:
        break
