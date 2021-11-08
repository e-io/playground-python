from list2block import list2block, str2block, md2block


def test_call_of_function():
    print('')
    print(str2block('the begin of output'))

    num = list2block()
    print(num)

    md2block("interests.md", "vk_interests_block.txt")
    print(str2block('the end of output'))


if __name__ == "__main__":
    test_call_of_function()

