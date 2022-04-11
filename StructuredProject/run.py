from ui import *
from dataset import *
from indexation import *
from filtering import *

data = getData()
dataIndex = getIndex(data)
#print(dataIndex)

res = getBooksByListOfIds(data, [2, 16245])
#print(res['Title'].values)

fOR, fAND = filterByRequest(dataIndex, "Ten Original")
#print(fOR, fAND)

startServer(dataIndex, data)