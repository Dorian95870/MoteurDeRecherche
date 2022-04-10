"""# Get DataSet"""
import pandas as pd


def getData():
  data = pd.read_csv('dataset/pg_catalog.csv', dtype={'Text#':int, 'Subjects':str})
  del data['Bookshelves']
  del data['LoCC']
  for i in range(len(data['Subjects'])):
    try:
      data['Subjects'][i] = data['Subjects'][i].split(';')
    except:
      del data['Subjects'][i]
  print('--------------DataSet Ready--------------')
  return data