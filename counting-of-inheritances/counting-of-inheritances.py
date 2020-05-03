import json

classes = json.load(open("classes2.json"))
# classes = json.loads(input())

inheritances = dict()
for class_ in classes:
    name = class_['name']
    if name not in inheritances:
        inheritances[name] = 1
    else:
        inheritances[name] += 1

    for parent in class_['parents']:
        if parent not in inheritances:
            inheritances[parent] = 1
        else:
            inheritances[parent] += 1

list_ = list(inheritances.keys())
list_.sort()
for class_ in list_:
    print(class_, ':', inheritances[class_])
