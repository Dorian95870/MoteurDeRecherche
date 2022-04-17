from indexation import *
from filtering import *

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
  listeOR,listeAND = filterByRequest(dataIndex,request)
  l3.extend(listeAND)
  l3.extend(listeOR)

  #enveler les doublons
  res= list()
  for i in l3:
   if i not in res:
    res.append(i)

  return res
