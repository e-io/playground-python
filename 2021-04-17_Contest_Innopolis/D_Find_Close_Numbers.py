def foo(inpt1, inpt2):
    array = list(map(lambda x: int(x), inpt2.split(' ')))
    array.sort()

    for n in range(len(array) - 1):
        if array[n] + 1 == array[n + 1]:
            return "YES"

    return "NO"


def test():
    tests = [("1", "7"), ("2", "4 3"), ("5", "11 1 8 13 14"), ("5", "4 10 8 5 9"), ("5", "5 5 5 5 5")]
    for n, ns in tests:
        print(n)
        print(ns)
        print(foo(n, ns))


def main():
    fst = input()
    snd = input()
    print(foo(fst, snd))


if __name__ == '__main__':
    # test()
    main()

# Accepted
