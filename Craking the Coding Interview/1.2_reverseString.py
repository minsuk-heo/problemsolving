import unittest

# pythonic way
def reverseString(str):
    return str[::-1]

# use stack to solve problem
def reverseString2(str):
    stack = []
    for ch in str:
        stack.append(ch)

    result = ""
    while len(stack) > 0:
        result += stack.pop()

    return result

class reverseStringTest(unittest.TestCase):
    def test(self):
        input = "abcde"
        self.assertEquals("edcba", reverseString(input))

        input = "qwert"
        self.assertEquals("trewq", reverseString2(input))