import unittest
import pandas as pd

class testData(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv('dataset/pg_catalog.csv', dtype={'Text#':int, 'Subjects':str})

    def testWrongPath(self):
        with self.assertRaises(FileNotFoundError):
            WrongPath = pd.read_csv('dataset.csv', dtype={'Text#':int, 'Subjects':str})

    def testCreationOfDataSet(self):
        self.assertIsInstance(self.data, pd.DataFrame)

    def testDataSetIsNotEmpty(self):
        self.assertIsNotNone(self.data,"dataset vide")

    def testDeleteNonExistantColoum(self):
        with self.assertRaises(KeyError) :
            del self.data[',ds']