"""# Filter"""
import re

def filterByRequest(dataIndex, request :str):
  #Definir nos règles de Filtrage
  
  wordsWithoutPonctuation = re.sub(r'[^\w\s]', '', request)
  words = wordsWithoutPonctuation.lower().split(' ')

  def getResOR():
    docsOR = list()
    for i in range(len(words)):
      try:
        docsOR += dataIndex[words[i]]
      except:
        print('Aucun résulats pour la requete: {}'.format(words[i]))
    return docsOR

  def getResAND():
    def intersection(lst1, lst2):
      lst3 = [value for value in lst1 if value in lst2]
      return lst3

    docsAND = list()
    for i in range(len(words)):
      try:
        docsAND.append(dataIndex[words[i]])
      except:
        print('Aucun résulats pour la requete: {}'.format(words[i]))
    res = list()
    for i in range(len(docsAND)):
      try:
        res = intersection(docsAND[i-1], docsAND[i])
      except:
        res = intersection(docsAND[i-1], docsAND[i])
    return res

  return (getResOR(), getResAND())