def test(*args):
    def add(*args):
        return args
    return add
print(test(1, 2, 3))
