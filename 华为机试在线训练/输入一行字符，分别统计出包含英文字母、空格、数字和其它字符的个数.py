while True:
    try:
        s = input()
        alpha_count = 0
        blank_count = 0
        number_count = 0
        other_count = 0
        for el in s:
            if el.isalpha():
                alpha_count += 1
            elif el == ' ':
                blank_count += 1
            elif el.isdigit():
                number_count += 1
            else:
                other_count += 1
        print(alpha_count)
        print(blank_count)
        print(number_count)
        print(other_count)
    except:
        break
