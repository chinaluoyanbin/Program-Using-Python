while True:
    try:
        n = int(raw_input())
        n -= 1
        count = 1
        value = 1
        while n >= count + 1:
            value += count - 1
            n -= count + 1
            count += 1
        value += n
        print(value)
    except:
        break
