# python 3-7-4

import csv

crimes = dict()
with open("crimes.csv") as file:
    detective = csv.reader(file)

    for row in detective:
        date = row[2]
        if "2015" in date:
            crime = row[5]
            if crime not in crimes:
                crimes[crime] = 1
            else:
                crimes[crime] += 1


counter = 1
while counter <= 10:
    max_ = 0
    max_crime = "no crime"
    for crime in crimes:
        if crimes[crime] > max_:
            max_ = crimes[crime]
            max_crime = crime

    print(counter, max_crime, max_)
    crimes.pop(max_crime)
    counter += 1
