from ui import *
from dataset import *
from indexation import *
from filtering import *
from ranking import *

data = getData()
dataIndex = getIndex(data)
#print(dataIndex)

#res = getBooksByListOfIds(data, [2, 16245])
#print(res['Authors'].values)

#fOR, fAND = filterByRequest(dataIndex, "Ten Original")
#print(fOR, fAND)

#rankingByAndOr(dataIndex, "scarlet car")

startServer(dataIndex, data)
