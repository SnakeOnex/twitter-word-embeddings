from flask import Flask, jsonify, json
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

""" @app.route("/<word>")
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
"""
@app.route("/<word>")
def getGay(word):
    rec_words = word.split('+')
    error_words = []
    emb_sum = []

    try:
        wid = word2id[rec_words[0]]
    except:
        error_words.append(rec_word)

    embedding = embs[wid:wid+1]

    d = cosine_similarity(embedding, embs)[0]
    d = zip(words, d)
    d = sorted(d, key=lambda x:x[1], reverse=True)
    similar_words = []
    for w in d[1:11]:
        similar_words.append(w)

    Xs = []
    Ys = []
    labels = []

    if len(rec_words) > 0:
        Y = np.load("tsne2.npy")
        #Y = np.load("pca.npy")

        print(rec_words)
        print('retard' in words)
        for label, x, y in zip(words, Y[:, 0], Y[:, 1]):
            if label == 'retard':
                print("LOOOL")
                
            if label in rec_words:
                print(label)
                Xs.append(str(x))
                Ys.append(str(y))
                labels.append(label)

    response = {"words": similar_words, "X": Xs, "Y": Ys, "labels": labels}
    jsonStr = json.dumps(response)
    #response = [similar_words, Xs, Ys]

    
    return jsonify(jsonStr)

        

if __name__=='__main__':
    embs, words, word2id = loadEmbs()
    app.run()
