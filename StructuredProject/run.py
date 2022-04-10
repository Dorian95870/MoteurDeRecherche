from ui import *
from dataset import *
from indexation import *

data = getData()
dataIndex = getIndex(data)

startServer(dataIndex, data)