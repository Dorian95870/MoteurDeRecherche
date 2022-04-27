from ui import *
from dataset import *
from indexation import *
from filtering import *
from ranking import *

data = getData()
dataIndex = getIndex(data)

startServer(dataIndex, data)
