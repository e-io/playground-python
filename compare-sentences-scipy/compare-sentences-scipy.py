from scipy import spatial
import re
import numpy as np

all_words = set()
text = []


def make_dictionary(line):
    text.append(line)
    words = re.split('[^a-z]', line.lower())
    sentence = dict()
    for word in words:
        if word == '':
            continue
        if word in sentence:
            sentence[word] += 1
        else:
            sentence[word] = 1

        all_words.add(word)

    return sentence


sentences = tuple(map(make_dictionary, open("sentences.txt")))
all_words = list(all_words)
all_words.sort()

matrix = np.zeros((len(sentences), len(all_words)))

for i in range(len(sentences)):
    for word in sentences[i]:
        matrix[i, all_words.index(word)] = sentences[i][word]

distances = dict()
for x in range(len(sentences)):
    distances[text[x]] = spatial.distance.cosine(matrix[0,], matrix[x,])

result = list(map(lambda i: rf"{distances[i]}: ({text.index(i)}){i}", distances))

result.sort()
for i in result:
    print(i)

#print(matrix[0,])
#print(matrix[4,])
#print(matrix[6,])
#answer: 4 6
