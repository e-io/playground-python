def foo(inpt):
    day = inpt[:3]
    num = int(inpt[4:])

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    result = days[(days.index(day) + num) % 7]

    return result


def test():
    print(foo("Sat 24"))


if __name__ == '__main__':
    # test()
    print(foo(input()))

# Accepted
