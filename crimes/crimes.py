import csv

crimes = dict()
with open("crimes.csv") as file:
    detective = csv.reader(file)
    counter = 0

    for row in detective:
        if "2015" in row[2] or counter == 0:
            # print(counter, ' ', row[2], ' ', row[5])
            crime = row[5]
            if crime not in crimes:
                crimes[crime] = 1
            else:
                crimes[crime] += 1
            # if counter == 50: break
            counter += 1

print(crimes)
max = 0
max_crime = "no crime"
for crime in crimes:
    if crimes[crime] > max:
        max = crimes[crime]
        max_crime = crime

print(max_crime, max)
