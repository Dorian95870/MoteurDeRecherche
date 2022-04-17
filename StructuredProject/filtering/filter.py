"""# Filter"""
import re

def filterByRequest(dataIndex, request :str):
  """Filter function : search all files in dataIndex that match with the request

  Args:
      dataIndex (_DataFrame_): _The dataIndex created witch contains all file word in a index_
      request (str): _The user request_

  Returns:
      _(List,List)_: _2 List one is the result of getresOR and the other is the result of getResAND_
  """
  #Definir nos règles de Filtrage
  
  wordsWithoutPonctuation = re.sub(r'[^\w\s]', '', request)
  words = wordsWithoutPonctuation.lower().split(' ')

  def getResOR():
    """Filter the list with OR

    Returns:
        _List_: _List result of OR filter_
    """
    docsOR = list()
    for i in range(len(words)):
      try:
        docsOR += dataIndex[words[i]]
      except:
        print('Aucun résulats pour la requete: {}'.format(words[i]))
    return docsOR

  def getResAND():
    """Filter the list with AND

    Returns:
        _List_: _List result of AND filter_
    """
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