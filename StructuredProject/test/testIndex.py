import unittest


class TestIndex(unittest.TestCase):
  
  # tester si l'id du mot bookshop est 172
  def test_Id(self):
    self.assertEqual('bookshop',self.data['Text#']==172)


if __name__ == '__main__':
    unittest.main()
