import unittest
from dataset.data import get_data


class TestIndex(unittest.TestCase):

    # tester si l'id du mot bookshop est 172
    def test_id(self):
        data = get_data()
        self.assertEqual('bookshop', self.data['Text#'] == 172)


unittest.main()
