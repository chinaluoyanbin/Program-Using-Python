base = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'elven', 'twelve', 'thirdteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen'
]

ty = {
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}


def num2word(n):
    """
    Parameters:
    -----------
        n: int, the number need to be tranlated to number

    Return:
    -------
        word: str, the target word
    """
    N = int(n)
    if 0 <= N <= 19:
        return base[N]
    if 20 <= N <= 99:
        if N % 10 == 0:
            return ty[n[0]]
        elif n[0] == '0':
            return num2word(n[1:])
        else:
            return ty[n[0]] + ' ' + num2word(n[1])
    if 100 <= N <= 999:
        if N % 100 == 0:
            return base[int(n[0])] + ' ' + 'hundred'
        else:
            return base[int(n[0])] + ' ' + 'hundred' + ' ' + 'and' + ' ' + num2word(n[1:])
    if 1000 <= N <= 999999:
        if N % 1000 == 0:
            return num2word(n[: 3]) + ' ' + 'thousand'
        elif len(n) == 4:
            return num2word(n[0]) + ' ' + 'thousand' + ' ' + num2word(n[1:])
        elif len(n) == 5:
            return num2word(n[: 2]) + ' ' + 'thousand' + ' ' + num2word(n[2:])
        else:
            return num2word(n[: 3]) + ' ' + 'thousand' + ' ' + num2word(n[3:])
    if 1000000 <= N <= 999999999:
        if N % 1000000 == 0:
            return num2word(n[: 3]) + ' ' + 'million'
        elif len(n) == 7:
            return num2word(n[0]) + ' ' + 'million' + ' ' + num2word(n[1:])
        elif len(n) == 8:
            return num2word(n[: 2]) + ' ' + 'million' + ' ' + num2word(n[2:])
        else:
            return num2word(n[: 3]) + ' ' + 'million' + ' ' + num2word(n[3:])
    return 'error'


while True:
    try:
        n = input()
        print(num2word(n))
    except:
        break
