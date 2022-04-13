import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv("pg_catalog.csv")

title = 'Title'

root = data[title][range(0,67583)]


for i in range(len(root)):
  documentA =  root[i]
  bagOfWordsA = documentA.split(' ')
  uniqueWords = set(bagOfWordsA).union(set(bagOfWordsA))
  numOfWordsA = dict.fromkeys(uniqueWords, 0)

  for word in bagOfWordsA : 
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

  try : 
    df = pd.DataFrame([tfidfA])
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([documentA])
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    print(df)
  except :
    print('marche pas')
