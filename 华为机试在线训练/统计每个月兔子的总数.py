def num_of_rabbits(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return num_of_rabbits(n - 1) + num_of_rabbits(n - 2)


while True:
    try:
        n = int(input())
        print(num_of_rabbits(n))
    except:
        break
