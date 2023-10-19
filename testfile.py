import unittest
from funct import myfunct
class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(myfunct(),0)
if __name__ == "__main__":
    unittest.main()
