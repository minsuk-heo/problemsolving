import unittest
"""
abbcccccccd -> a1b2c7d1
abc -> abc if the compression (a1b1c1) is longer than original, return original
"""

def compressword(input):
    buffer = None
    output = ""
    cnt = 1
    for ch in input:
        if buffer is None:
            output += ch
            buffer = ch
        else:
            if buffer == ch:
                cnt = cnt + 1
            else:
                output += str(cnt)
                cnt = 1
                output += ch
                buffer = ch
    output += str(cnt)

    if len(output) > len(input):
        return input
    else:
        return output

class compress_test(unittest.TestCase):
    def test(self):
        self.assertEqual("a1b2c7d1",compressword("abbcccccccd"))
        self.assertEqual("a1b7c2d2", compressword("abbbbbbbccdd"))
        self.assertEqual("abc", compressword("abc"))
        self.assertEqual("aabcc", compressword("aabcc"))