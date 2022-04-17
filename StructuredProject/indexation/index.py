"""# Index"""
import re
import pandas as pd

def getIndex(data):
  """Get all informations in data to make a word index

  Args:
      data (_DataFrame_): _All the data got from the CSV File_

  Returns:
      _dict_: _Dict of Word and their Book id /position in title_
  """
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
  """Get All book that matchs with the specific list of ids : ids

  Args:
      data (_DataFrame_): _The data we need to explore_
      ids (list): _List of ids to find in data_

  Returns:
      _DataFrame: _A smaller DataFrame with the ids we searched for_
  """
  books = dict()
  for key in data.keys():
    books[key] = list()

  for i in range(len(ids)):
    for key in data.keys():
      books[key].append(data.loc[data['Text#'] == ids[i]][key].values)
  res = pd.DataFrame(books)
  return res

