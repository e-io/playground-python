def foo(inpt):
    a, b = list(map(lambda x: int(x), inpt.split(' ')))

    if a + b <= 3:
        return 0

    if b < a:
       a, b = b, a

    if b >= 4 * a:
        return b // 4

    if b >= 3 * a:
        return b // 3

    var1 = a // 2
    var2 = b // 3

    return max(var1, var2)
    

def test():
    tests = ["10 21", "13 11", "2 1", "1 8", "3 8", "2 2", "100 101", "20 10"]
    for tst in tests:
        print(tst)
        print(foo(tst))
        print(' ')


if __name__ == '__main__':
    # test()
    print(foo(input()))

    # failed on test 25
