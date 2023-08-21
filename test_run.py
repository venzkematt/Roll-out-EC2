import unittest
from run import checkInt

class TestCheckInt(unittest.TestCase):
    def test_checkInt(self):
        self.assertEqual (checkInt(type(9.0)), int)

if __name__ == "__main__":
    unittest.main()
