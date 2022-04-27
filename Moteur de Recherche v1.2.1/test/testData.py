import unittest
import pandas as pd


class testData(unittest.TestCase):
    def set_up(self):
        self.data = pd.read_csv('dataset/pg_catalog.csv',
                                dtype={'Text#': int, 'Subjects': str})

    def test_wrong_path(self):
        with self.assertRaises(FileNotFoundError):
            WrongPath = pd.read_csv('dataset.csv', dtype={
                                    'Text#': int, 'Subjects': str})

    def test_creation_of_dataset(self):
        self.assertIsInstance(self.data, pd.DataFrame)

    def test_dataset_is_not_empty(self):
        self.assertIsNotNone(self.data, "dataset vide")

    def test_delete_non_existant_coloum(self):
        with self.assertRaises(KeyError):
            del self.data[',ds']
