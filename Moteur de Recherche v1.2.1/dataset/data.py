"""# Get DataSet"""
import pandas as pd
import requests
import time


def get_data(path):
    """Read CSV File and get all data inside in pandas DataFrame format

    Returns:
        _DataFrame_: _Table that contain all CSV file data_
    """
    data = pd.read_csv(path,
                       dtype={'Text#': int, 'Subjects': str, 'Type': str, 'Title': str, 'Language': str, 'Authors': str}, usecols=range(7))

    for subject in data['Subjects']:
        if type(subject) == str:
            subject = subject.split(';')
        else:
            subject = pd.NaT
    print('--------------Extracting Data--------------')
    data = _get_download_count(data)
    print('--------------DataSet Ready--------------')
    return data


def _extract_data_from_interval_of_ids(data, start, ammount):
    url = 'https://gutendex.com/books?ids='
    ids = ','.join(str(i) for i in data['Text#'][start:start+ammount])

    download_data = requests.get(url+ids)
    download_data = download_data.json()

    for i in range(len(download_data['results'])):
        data.loc[data['Text#'] == download_data['results'][i]['id'],
                 'download_count'] = download_data['results'][i]['download_count']


def _get_download_count(data):
    t = time.process_time()
    data_per_request = 1000
    data['download_count'] = pd.NaT

    for x in range(0, len(data), data_per_request):
        _extract_data_from_interval_of_ids(data, x, data_per_request)
        print(
            f'{int((x/len(data))*100)}% - {x}/{len(data)} - {round((time.process_time() - t) * 10)}s')

    return data
