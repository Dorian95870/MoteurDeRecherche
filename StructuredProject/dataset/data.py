"""# Get DataSet"""
import pandas as pd


def getData():
  """Read CSV File and get all data inside in pandas DataFrame format

  Returns:
      _DataFrame_: _Table that contain all CSV file data_
  """
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