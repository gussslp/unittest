import unittest

def lst(st):
    a = list(st)
    return a


class Testlst(unittest.TestCase):
    def test_lst_success(self):
        actual = lst("monke")
        expected = ["m","o","n","k","e",]
        self.assertEqual(actual, expected)

    