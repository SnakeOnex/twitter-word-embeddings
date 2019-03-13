from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import sys

f = open(sys.argv[1])
f.readline()

embeddings = []
words = []
word2id = dict()

for i, line in enumerate(f):
    line = line.strip().split(' ')
    word=line[0]
    embedding = [float(x) for x in line[1:]]
    assert len(embedding) == 100
    embeddings.append(embedding)
    words.append(word)
    word2id[word] = i
    print(str(i) + " "+ word)

embeddings = np.array(embeddings)
while True:
    word = input('Word: ')
    try:
        wid = word2id[word]
    except:
        print('Cannot find this word')
        continue

    embedding = embeddings[wid:wid+1]
    d = cosine_similarity(embedding, embeddings)[0]
    d = zip(words, d)
    d = sorted(d, key=lambda x:x[1], reverse=True)
    for w in d[:10]:
        print(w)


