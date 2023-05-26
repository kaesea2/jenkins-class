import unittest2 as ut
from .test import add,mul,div
class MyTest(ut.TestCase):
    def test_add(self):
        test = add(5, 7)
        expected = 12
        self.assertEqual(test,expected)
        
    def test_mul(self):
        test = mul(5, 7)
        expected = 35
        self.assertEqual(test,expected)
        
ut.main()
# if __name__ == '__main__':
#     unittest.main()