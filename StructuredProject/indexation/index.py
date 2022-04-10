"""# Index"""
import re

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
        dataIndex[word].append(docId)
      except:
        dataIndex[word] = list()
        dataIndex[word].append(docId)
  print('--------------Index Created--------------')
  return dataIndex

def getBooksByListOfIds(data, ids: list()):
  books = list()
  for i in range(len(ids)):
    books.append(data.loc[data['Text#'] == ids[i]])
  return books

