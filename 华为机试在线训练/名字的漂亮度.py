def max_beauty_of_name(name):
    rank = list(set(name))
    rank.sort(key=name.count, reverse=True)
    maxValue = 0
    for el in name:
        maxValue += 26 - rank.index(el)
    return maxValue


while True:
    try:
        N = int(input())
        for i in range(N):
            print(max_beauty_of_name(input()))
    except:
        break
