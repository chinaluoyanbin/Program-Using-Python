def is_valid(lyst):
    if len(lyst) != 4:
        return False
    elif lyst[0] < '0' or lyst[0] > '255' or lyst[1] < '0' or lyst[1] > '255' or lyst[2] < '0' or lyst[2] > '255' or lyst[3] < '0' or lyst[3] > '255':
        return False
    else:
        return True


def is_valid_mask(s):
    left = s.index('0')
    if '1' in s[left:]:
        return False
    else:
        return True


def is_same_host(mask, ip1, ip2):
    if is_valid(mask) and is_valid(ip1) and is_valid(ip2):
        m = ''
        for el in mask:
            m += bin(int(el)).replace('0b', '').rjust(8, '0')
        if is_valid_mask(m):
            i1 = ''
            for el in ip1:
                i1 += bin(int(el)).replace('0b', '').rjust(8, '0')
            i2 = ''
            for el in ip2:
                i2 += bin(int(el)).replace('0b', '').rjust(8, '0')
            host1, host2 = '', ''
            for i in range(32):
                host1 += str(int(i1[i]) & int(m[i]))
                host2 += str(int(i2[i]) & int(m[i]))
            if host1 == host2:
                return 0
            else:
                return 2
        else:
            return 1
    else:
        return 1


while True:
    try:
        """这道题的测试样例有毒！"""
        mask = input().split('.')
        ip1 = input().split('.')
        ip2 = input().split('.')
        print(is_same_host(mask, ip1, ip2))
    except:
        break
