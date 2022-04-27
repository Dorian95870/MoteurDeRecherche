import unittest
import pandas as pd
from filtering.filter import filter_by_request


class testFilter(unittest.TestCase):
    def set_up(self):
        self.data = pd.read_csv('dataset/pg_catalog.csv',
                                dtype={'Text#': int, 'Subjects': str})

    def test_special_caracter(self):
        filter_by_request(self.data, "!")

    def test_2_words_request(self):
        filter_by_request(self.data, "crimson car")

    def test_random_type(self):
        filter_by_request(self.data, "sdjize")
