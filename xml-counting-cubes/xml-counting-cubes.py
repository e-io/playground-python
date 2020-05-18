from xml.etree import ElementTree

from_file = True

sum = {
    "red": 0,
    "green": 0,
    "blue": 0
}


def add_and_go_to_children(cube, step):
    sum[cube.attrib["color"]] += step
    for child in cube:
        add_and_go_to_children(child, step + 1)


if from_file:
    root = ElementTree.parse("input.txt").getroot()
else:
    root = ElementTree.fromstring(input())

add_and_go_to_children(root, 1)

for color in sum:
    print(f"{color}: {sum[color]}")
