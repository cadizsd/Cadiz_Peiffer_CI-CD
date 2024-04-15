import unittest

from main import main


class MyTestCase(unittest.TestCase):
    def test_add(self):
        obj = main(1, 2, 3)
        self.assertEqual(obj.add(), 6)


if __name__ == '__main__':
    unittest.main()
