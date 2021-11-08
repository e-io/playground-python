
def str2block(string, width=40):
    for s in {' ', '-'}:
        string = string.replace(s, '_')
    max = width
    result = f'{{:_^{max}}}'.format(string)
    return(result)

def list2block(md='', width=40):
    print("I am 'list2block'")
    return 42



def md2block(input, output, width=40):

    with (
            open(input, "r") as md,
            open(output, "w") as txt,
    ):

            txt.writelines([str2block('', width=width), '\n'])

            lines = md.read().split('\n')
            for line in lines:

                match line.split(' ', 1):
                    case '#', essence:
                        line = '<' + essence.upper() + '>'
                    case '##'|'###', essence:
                        line = essence.upper()
                    case '-'|'*', essence:
                        line = essence
                    case beginning, essence:
                        # all other beginnigs treat as part of essence. No action needed (line == line)
                        pass
                    case _:
                        pass
                result = str2block(line, width=width)

                txt.writelines ([result, '\n'])

            txt.write(str2block('', width=width))

            print('i am here')





