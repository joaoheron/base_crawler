import unittest

class TestExample(unittest.TestCase):

    def test_example(self):
        print('Running test_example...')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
