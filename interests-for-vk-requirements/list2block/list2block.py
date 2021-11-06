
def str2block(string, width=40):
    for s in {' ', '-'}:
        string = string.replace(s, '_')
    max = width
    result = f'{{:_^{max}}}'.format(string)
    return(result)

def list2block(json='', width=40):
    return 42
    print("I am 'list2block'")