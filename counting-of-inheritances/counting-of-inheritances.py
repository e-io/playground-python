import json

classes = json.load(open("classes5.json"))
# classes = json.loads(input())

inheritances = dict()
for class_ in classes:
    name = class_['name']

    if name not in inheritances:
        inheritances[name] = set()

    for parent in class_['parents']:
        if parent not in inheritances:
            inheritances[parent] = set(name)
        else:
            inheritances[parent].add(name)


def all_children(parent):
    children = inheritances[parent]
    all_children_ = set()
    for child in children:
        all_children_ .add(child)
        results = all_children(child)
        for result in results:
            all_children_ .add(result)
    return all_children_


for parent in inheritances:
    all_children_ = set()
    all_children_ = all_children(parent)
    inheritances[parent] = all_children_
    
list_ = list(inheritances.keys())
list_.sort()
for parent in list_:
    print(parent, ':', len(inheritances[parent]) + 1)
