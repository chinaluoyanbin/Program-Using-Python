while True:
    try:
        ip = input().split('.')
        n = int(input())
        # ip -> int
        s = ''
        for el in ip:
            s += bin(int(el)).replace('0b', '').rjust(8, '0')
        print(int(s, 2))
        # int -> ip
        s = bin(n).replace('0b', '').rjust(32, '0')
        ip = []
        for i in range(0, 32, 8):
            ip.append(str(int(s[i: i + 8], 2)))
        print('.'.join(ip))
    except:
        break
