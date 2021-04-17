def foo(inpt):
    for n in range(len(inpt) - 3, -1, -1):
        if inpt[n] == inpt[n + 1] and inpt[n] == inpt[n + 2]:
            inpt = inpt[0:n + 2] + inpt[n + 3:]

    result = inpt

    return result


def test():
    tests = ["eedaaad", "xxxtxxx", "uuuuxaaaaxuuu", "uuuxxffffasssss", "abc", "u", "ab", "aaa", "aa", "aaaaaaaaaaa"]
    for s in tests:
        print(foo(s))


if __name__ == '__main__':
    # test()
    print(foo(input()))

# Accepted
