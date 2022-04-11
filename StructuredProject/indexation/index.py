"""# Index"""
import re
import pandas as pd

def getIndex(data):
  root = 'Title'
  dataIndex = dict()
  for i in range(len(data[root])):
    docId = data['Text#'][i]
    words = data[root][i].split(' ')
    for y in range(len(words)):
      wordsWithoutPonctuation = re.sub(r'[^\w\s]', '', words[y])
      word = wordsWithoutPonctuation.lower()
      try:
        dataIndex[word][docId].append(y)
      except:
        try:
          dataIndex[word][docId] = list()
          dataIndex[word][docId].append(y)
        except:
          dataIndex[word] = dict()
          dataIndex[word][docId] = list()
          dataIndex[word][docId].append(y)
  print('--------------Index Created--------------')
  return dataIndex

def getBooksByListOfIds(data, ids: list()):
  books = dict()
  for key in data.keys():
    books[key] = list()

  for i in range(len(ids)):
    for key in data.keys():
      books[key].append(data.loc[data['Text#'] == ids[i]][key].values)
  res = pd.DataFrame(books)
  return res

