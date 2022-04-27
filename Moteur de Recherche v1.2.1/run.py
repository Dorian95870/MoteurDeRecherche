from ui import start_server
from dataset import get_data
from indexation import get_index

data = get_data('dataset/pg_catalog.csv')
data_index = get_index(data)
start_server(data_index, data)
