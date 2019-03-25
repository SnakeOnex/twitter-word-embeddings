from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
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

tsne = TSNE(n_components=2, random_state=0)
Y = tsne.fit_transform(embeddings[:50])

plt.scatter(Y[:, 0], Y[:, 1])
for label, x, y in zip(words, Y[:, 0], Y[:, 1]):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
plt.show()


