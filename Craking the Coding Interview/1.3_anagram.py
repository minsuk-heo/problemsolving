import unittest

"""
anagram: true if listen and silent
better ask if space is considered as string
uppercase is different from lowercase
"""

def anagram(str1, str2):
    if ''.join(sorted(str1.lower())).strip() == ''.join(sorted(str2.lower())).strip():
        return True
    else:
        return False

class anagramTest(unittest.TestCase):
    def test(self):
        self.assertTrue(anagram("listen", "silent"))
        self.assertFalse(anagram("abc", "def"))



