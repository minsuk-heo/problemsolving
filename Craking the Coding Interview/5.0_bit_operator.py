import unittest

"""
num  = 10 (1010)
"""
def getBit(num, idx):
    if num & (1 << idx) != 0:
        return 1
    else:
        return 0

def setBit(num, idx):
    return num | (1 << idx)

def clearBit(num, idx):
    return num & ~(1 << idx)

def clearBitsMSBThroughIdx(num, idx):
    mask = (1 << idx) - 1
    return num & mask

class bittest(unittest.TestCase):
    def test(self):
        # 10 = 1010 in decimal expression

        #getBit test
        self.assertEqual(0, getBit(10, 0))
        self.assertEqual(1, getBit(10, 1))
        self.assertEqual(0, getBit(10, 2))
        self.assertEqual(1, getBit(10, 3))
        # setBit test
        self.assertEqual(11, setBit(10, 0))
        self.assertEqual(10, setBit(10, 1))
        self.assertEqual(14, setBit(10, 2))
        # clearBit test
        self.assertEqual(10, clearBit(10, 0))
        self.assertEqual(8, clearBit(10, 1))
        self.assertEqual(10, clearBit(10, 2))
        self.assertEqual(2, clearBit(10, 3))
        # clearBitsMSBThroughIdx test
        self.assertEqual(0, clearBitsMSBThroughIdx(10, 0)) #0000
        self.assertEqual(0, clearBitsMSBThroughIdx(10, 1)) #0000
        self.assertEqual(2, clearBitsMSBThroughIdx(10, 2)) #0010
        self.assertEqual(2, clearBitsMSBThroughIdx(10, 3)) #0010

