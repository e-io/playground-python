def foo(inpt1, inpt2):
    array = list(map(lambda x: int(x), inpt2.split(' ')))

    n = 0
    cnt = 0

    for i in range(len(array) - 1):
        n += 2 ** (array[i] - 1)
        if n & (n + 1) == 0:
            cnt += 1

    # last number will give 1 anyway
    return str(cnt + 1)


def test():
    tests = [("5", "2 1 3 5 4", "3"), ("5", "2 3 4 1 5", "2"), ("5", "1 3 4 2 5", "3")]
    for n, ns, crct_ans in tests:
        print(n)
        print(ns)
        ans = foo(n, ns)
        print(ans)
        print('YES') if ans == crct_ans else print('NO')
        print()


def main():
    fst = input()
    snd = input()
    print(foo(fst, snd))


if __name__ == '__main__':
    # test()
    main()

# Accepted
