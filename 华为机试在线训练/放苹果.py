def func(m, n):
    """
    把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
    
    Parameters:
    -----------
        m: int, 苹果个数
        n: int, 盘子个数
    
    Return:
    -------
        num: int, 放置方法总数
    """
    if m == 0 or n == 1:
        return 1
    elif m < n:
        return func(m, m)
    else:
        return func(m, n - 1) + func(m - n, n)


while True:
    try:
        m, n = map(int, input().split())
        print(func(m, n))
    except:
        break
