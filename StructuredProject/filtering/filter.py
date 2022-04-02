"""# Filter"""
import re

def filterByRequest(dataIndex, request :str):
  #Definir nos règles de Filtrage
  docs = list()
  
  wordsWithoutPonctuation = re.sub(r'[^\w\s]', '', request)
  words = wordsWithoutPonctuation.lower().split(' ')
  for i in range(len(words)):
    try:
      docs += dataIndex[words[i]]
    except:
      print('Aucun résulats pour la requete: {}'.format(words[i]))
  return docs, len(docs)