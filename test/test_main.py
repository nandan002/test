import unittest
from src.test import add
class TestMain(unittest.TestCase):
  def test_add(self):
    self.assert.Equal(add(1,2),3)

if __name__ == "__main__":
  unitest.main()
