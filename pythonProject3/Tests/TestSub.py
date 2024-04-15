import unittest

from sub import sub


class MyTestCase(unittest.TestCase):
    def test_something(self):
        obj = sub(1, 2, 3)
        self.assertEqual(obj.sub(), -4)


if __name__ == '__main__':
    unittest.main()
