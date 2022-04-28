import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def _compute_tf(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict


def _compute_idf(documents):
    import math
    N = len(documents)

    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict


def _compute_tfidf(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf


def get_tfidf(data):
    title = 'Title'
    root = data[title][range(0, 67583)]
    res = dict()

    print('--------------Creating TF-IDF--------------')
    for i in range(len(root)):
        documentA = root[i]
        bagOfWordsA = documentA.split(' ')
        uniqueWords = set(bagOfWordsA).union(set(bagOfWordsA))
        numOfWordsA = dict.fromkeys(uniqueWords, 0)

        for word in bagOfWordsA:
            numOfWordsA[word] += 1

        tfA = _compute_tf(numOfWordsA, bagOfWordsA)
        idfs = _compute_idf([numOfWordsA])
        tfidfA = _compute_tfidf(tfA, idfs)

        vectorizer = TfidfVectorizer()
        is_valid = True
        try:
            vectors = vectorizer.fit_transform([documentA])
        except:
            is_valid = False
        if is_valid:
            feature_names = vectorizer.get_feature_names_out()
            dense = vectors.todense()
            denselist = dense.tolist()
            doc_id = data["Text#"][i]

            if doc_id not in res.keys():
                res[doc_id] = dict()
            for feature in feature_names:
                if feature not in res[doc_id].keys():
                    res[doc_id][feature] = list()
                res[doc_id][feature].append(denselist)
    print('--------------TF-IDF Created--------------')
    return res
