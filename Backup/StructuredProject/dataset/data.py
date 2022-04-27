"""# Get DataSet"""
import pandas as pd
import requests
import time


def getData():
    """Read CSV File and get all data inside in pandas DataFrame format

    Returns:
        _DataFrame_: _Table that contain all CSV file data_
    """
    data = pd.read_csv('dataset/pg_catalog.csv',
                       dtype={'Text#': int, 'Subjects': str})
    del data['Bookshelves']
    del data['LoCC']
    for i in range(len(data['Subjects'])):
        try:
            data['Subjects'][i] = data['Subjects'][i].split(';')
        except:
            del data['Subjects'][i]
    print('--------------Extracting Data--------------')
    data = getDownloadCount(data)
    print('--------------DataSet Ready--------------')
    return data


def getDownloadCount(data):
    t = time.process_time()
    url = 'https://gutendex.com/books?ids='
    dataPerRequest = 1000
    data['download_count'] = pd.NaT

    def extractDataFromIntervalOfIds(start, ammount):
        print('{}% - {}/{} - {}s'.format(int((start/len(data))*100),
              start, len(data), round((time.process_time() - t) * 10)))
        ids = ','.join(str(i) for i in data['Text#'][start:start+ammount])

        downloadData = requests.get(url+ids)
        downloadData = downloadData.json()

        for i in range(len(downloadData['results'])):
            data.loc[data['Text#'] == downloadData['results'][i]['id'],
                     'download_count'] = downloadData['results'][i]['download_count']
    for x in range(0, len(data), dataPerRequest):
        extractDataFromIntervalOfIds(x, dataPerRequest)

    return data

    # print(downloadData['results'][0]['download_count'])
