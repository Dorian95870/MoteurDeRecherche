import unittest
import pandas as pd
from filtering.filter import filterByRequest

class testFilter(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv('dataset/pg_catalog.csv', dtype={'Text#':int, 'Subjects':str})
        
    def testSpecialCaracter(self):
        filterByRequest(self.data,"!")
        
    def test2WordsRequest(self):
        filterByRequest(self.data,"crimson car")