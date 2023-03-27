import unittest

def is_palindrome(word):
    reverse_word = word[::-1]
    if reverse_word == word:
        return "word %s is palindrome" % word
    else:
        return "word %s isn't palindrome" % word

class Testlst(unittest.TestCase):
    def test_lst_success(self):
        actual = is_palindrome("deified")
        expected = "word deified is palindrome"
        self.assertEqual(actual, expected)


