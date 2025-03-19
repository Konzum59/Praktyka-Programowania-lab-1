import unittest
from main import Add

class testing(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(""), 0)
    def test_single(self):
        self.assertEqual(Add("1"), 1)
    def test_double(self):
        self.assertEqual(Add("1,2"), 3)
    def test_more(self):
        self.assertEqual(Add("1,2,3"), 6)
    def test_new_line(self):
        self.assertEqual(Add("1\n2,3"), 6)
    def test_add_error(self):
        self.assertEqual(Add("1,\n2,3"), "!", "wrong input >:[")



