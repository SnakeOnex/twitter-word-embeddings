from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
app = Flask(__name__)
CORS(app)

def loadEmbs():
    f = open("embs.txt")
    f.readline()

    embeddings = []
    words = []
    word2id = dict()

    for i, line in enumerate(f):
        line = line.strip().split(' ')
        word = line[0]
        embedding = [float(x) for x in line[1:]]
        assert len(embedding) == 64
        embeddings.append(embedding)
        words.append(word)
        word2id[word] = i
        print(str(i) + " " + word)
    embeddings = np.array(embeddings)
    return embeddings, words, word2id



embs = []
words = []
word2id = dict()

embs, words, word2id = loadEmbs()

@app.route('/')
def display():
    return "no word"

@app.route("/<word>")
def getMember(word):
    try:
        wid = word2id[word]
    except:
        return "does not exist"

    embedding = embs[wid:wid+1]
    d = cosine_similarity(embedding, embs)[0]
    d = zip(words, d)
    d = sorted(d, key=lambda x:x[1], reverse=True)
    similar_words = []
    for w in d[1:11]:
        similar_words.append(w)
    return jsonify(similar_words)

if __name__=='__main__':
    embs, words, word2id = loadEmbs()
    app.run()
