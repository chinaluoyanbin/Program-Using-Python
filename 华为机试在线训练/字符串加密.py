Alphabet = [chr(i) for i in range(65, 91)]

while True:
    try:
        s = input().upper()
        key = []
        for el in s:
            if el not in key:
                key.append(el)
        for el in Alphabet:
            if el not in key:
                key.append(el)
        mi = input()
        ming = []
        for el in mi:
            if el.isupper():
                ming.append(key[Alphabet.index(el)])
            else:
                ming.append(key[Alphabet.index(el.upper())].lower())
        print(''.join(ming))
    except:
        break
