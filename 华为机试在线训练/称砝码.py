def number_of_weights(n, m, x):
    """
    Parameters:
    -----------
        n: int, 砝码个数
        m: list, 单个砝码的重量
        x: list, 单个砝码的数量

    Return:
    -------
        num: int, 砝码组合不同重量的个数
    """
    weights = set()  # 砝码重量集合
    for i in range(x[0] + 1):  # 先把第一个砝码组合的不同重量加入到集合中
        weights.add(i * m[0])
    for i in range(1, n):  # 从第二个砝码开始, 0~n
        temp = list(weights)  # set转换成list, list可以遍历, set不可以
        for j in range(1, x[i] + 1):  # 砝码个数, 1 ~ x[i] + 1
            for t in temp:  # 集合中已有的重量
                weights.add(t + j * m[i])  # 集合中已有的重量加上新增加的j个砝码的重量
    return len(weights)


while True:
    try:
        n = int(input())
        m = [int(i) for i in input().split()]
        x = [int(i) for i in input().split()]
        print(number_of_weights(n, m, x))
    except:
        break
