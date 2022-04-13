from indexation import *
from filtering import *

# classer en premier pour les documents qui contient plus de mots dans la requete
def rankingByAndOr(dataIndex, request :str):

  l3 = list()
  listeOR,listeAND = filterByRequest(dataIndex,request)
  l3.insert(0,listeAND)
  l3.extend(listeOR)

  #enveler les doublons
  res= list()
  for i in l3:
   if i not in res:
    res.append(i)

  return res
