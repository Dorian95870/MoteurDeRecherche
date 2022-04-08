"""Ranking"""

#classer les resultats de la requete par ordre chronologique
for i in getBooksByListOfIds(dataRes): 
  print(i.sort_values(by='Issued'))
  