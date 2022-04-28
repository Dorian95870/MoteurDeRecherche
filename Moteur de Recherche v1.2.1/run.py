from ui import start_server
from dataset import get_data
from indexation import get_index
from termFrequency import get_tfidf

data = get_data('dataset/pg_catalog.csv')
data_index = get_index(data)
tfidf = get_tfidf(data)

start_server(data_index, data, tfidf)
