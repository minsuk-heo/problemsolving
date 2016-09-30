import unittest

def insertion_sort(input):

    for idx, valueToInsert in enumerate(input):
        # select the hole position where number is to be inserted
        holePosition = idx

        # check if previous no. is larger than value to be inserted
        while holePosition > 0 and input[holePosition-1] > valueToInsert:
            input[holePosition - 1], input[holePosition] = input[holePosition], input[holePosition-1]
            holePosition = holePosition - 1

    return input

class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([6, 5, 4, 3, 2, 1]))