import math


def insert_item(low, high, mat):
    step = math.trunc((mat[-1][1] - mat[0][1]) / (mat[-1][0] - mat[0][0]))
    for i in range(1, el[0] - temp[0]):
        mat.insert(mat.index(high), [temp[0] + i, temp[1] + step * i])


while True:
    try:
        m, n = map(int, input().split())
        mat = []
        for i in range(m):
            mat.append(list(map(int, input().split())))
        temp = mat[0]
        for el in mat[1:]:
            if el[0] > temp[0] + 1:
                insert_item(temp, el, mat)
                temp = el
            if el[0] == temp[0]:
                mat.pop(mat.index(el))
        for el in mat:
            print('%d %d' % (el[0], el[1]))
    except:
        break
