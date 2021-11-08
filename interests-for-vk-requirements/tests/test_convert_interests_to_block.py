from list2block.list2block import list2block, str2block


def test_call_of_function():
    print('')
    print(str2block('the begin of output'))
    num = list2block()

    print(num)
    print(str2block('the end of output'))


if __name__ == "__main__":
    test_call_of_function()

