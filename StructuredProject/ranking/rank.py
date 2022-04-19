from indexation import *
from filtering import *
from enum import Enum
from datetime import datetime


# classer en premier pour les documents qui contient plus de mots dans la requete
def rankingByAndOr(dataIndex, request :str):
  """_ranking of the results by and fisrt and then by or_

  Args:
      dataIndex (_dict_): _the dataIndex we are using of or website_
      request (str): _the user request_

  Returns:
      _List_: _List of results with AND results first and Or after_
  """

  l3 = list()
  listOR,listAND = filterByRequest(dataIndex,request)
  l3.extend(listAND)
  l3.extend(listOR)

  #enveler les doublons
  listOfIds= list()
  for i in l3:
   if i not in listOfIds:
    listOfIds.append(i)
  
  return listOR,listAND, listOfIds

def score(data, dataIndex, request :str):
  class Values(Enum):
    AND = 10
    OR = 5
    DATE = 2

  listOR,listAND, listOfIds = rankingByAndOr(dataIndex, request)

  # vvvvvv Scoring vvvvvv

  res = dict.fromkeys(listOfIds, 0)
  docsInfos = getBooksByListOfIds(data, listOfIds)

  # Score par type de filtrage
  for doc in listOR:
    res[doc] = Values.OR.value
  for doc in listAND:
    res[doc] = Values.AND.value

  for i, doc in enumerate(listOfIds):
    tempDoc = docsInfos.loc[docsInfos['Text#'] == doc]

    # Score par date
    if datetime.strptime(tempDoc['Issued'][i][0], '%Y-%m-%d') >= datetime.strptime('2013-01-01', '%Y-%m-%d'):
      res[doc] += Values.DATE.value
      print(tempDoc['Issued'].values)

  return res

