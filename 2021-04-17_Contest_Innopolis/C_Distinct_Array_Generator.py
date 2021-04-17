def foo(inpt):
    result = []
    for n in range(1, inpt // 2 + 1):
        result.append(-n)
        result.append(n)

    if inpt % 2 == 1:
        result.append(0)

    rng = ""
    for n in result[0:-1]:
        rng += (str(n) + ' ')

    rng += str(result[-1])

    return rng


def test():
    tests = [1, 2, 3, 4, 5, 6, 7, 21]
    for n in tests:
        print(foo(n))


if __name__ == '__main__':
    # test()
    print(foo(int(input())))

# Accepted
