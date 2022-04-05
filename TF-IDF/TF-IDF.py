import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documentA = 'The Declaration of Independence of the United States of Americ The United States Bill of Rights The Ten Original Amendments to the Constitution of the United States John F. Kennedys Inaugural Address Lincolns Gettysburg Address Given November 19, 1863 on the battlefield near Gettysburg, Pennsylvania, USA The United States Constitution Give Me Liberty or Give Me Death The Mayflower Compact Abraham Lincolns Second Inaugural Address Abraham Lincolns First Inaugural Address The King James Version of the Bible Alices Adventures in Wonderland Through the Looking-Glass The Hunting of the Snark: An Agony in Eight Fits The 1990 CIA World Factbook Moby-Dick; or, The Whale Peter Pan The Book of Mormon An Account Written by the Hand of Mormon, Upon Plates Taken from the Plates of Nephi The Federalist Papers The Song of Hiawatha Paradise Lost'

# Extraire les caractéristiques du texte
bagOfWordsA = documentA.split(' ')

# Supprime automatiquement tout mot en double.
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsA))

# Créer un dictionnaire des mots et de leur occurrence pour chaque document du corpus
numOfWordsA = dict.fromkeys(uniqueWords, 0)

for word in bagOfWordsA:
    numOfWordsA[word] += 1

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

tfA = computeTF(numOfWordsA, bagOfWordsA)

def computeIDF(documents):
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

idfs = computeIDF([numOfWordsA])

def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfidfA = computeTFIDF(tfA, idfs)

df = pd.DataFrame([tfidfA])

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([documentA])
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)

df.head()
