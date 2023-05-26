import unittest as ut
import test as t

class MyTest(ut.TestCase):
    def test_add(self):
        test = t.add(5, 7)
        expected = 12
        self.assertEqual(test,expected)
        
    def test_mul(self):
        test = t.mul(5, 7)
        expected = 35
        self.assertEqual(test,expected)
        
if __name__ == '__main__':
    ut.main()