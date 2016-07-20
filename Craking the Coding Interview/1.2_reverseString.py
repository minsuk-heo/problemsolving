import unittest

def reverseString(str):
    return str[::-1]

class reverseStringTest(unittest.TestCase):
    def test(self):
        input = "abcde"
        self.assertEquals("edcba", reverseString(input))