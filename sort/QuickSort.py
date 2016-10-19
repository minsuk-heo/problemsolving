import unittest

def quick_sort(list, start, end):
    # repeat until sublist has one item
    # because the algorithm is using in-place space, we can not use len(list) instead we use start, end for sublist
    if start < end:
        # get pivot using partition method
        pivot = partition(list, start, end)
        # recurse quick sort left side from pivot
        quick_sort(list, start, pivot-1)
        # recurse quick sort right side from pivot
        quick_sort(list,pivot+1, end)
    return list

def partition(list, start, end):
    # use end item as initial pivot
    pivot = end
    # use start as initial wall index
    wall = start
    left = start
    # repeat until left item hit the end of list
    while left < pivot:
        # if left item is smaller than pivot, swap left item with wall and move wall to right
        # this will ensure items smaller than pivot stay left side from the wall and
        # the items greater than pivot stay right side from the wall
        if list[left] < list[pivot]:
            list[wall], list[left] = list[left], list[wall]
            wall = wall + 1
        left = left + 1
    # when left hit the end of list, swap pivot with wall
    list[wall], list[pivot] = list[pivot], list[wall]
    # now left side of wall are the items smaller than wall
    # now right side of pivot are the items greater than wall
    # wall is the new pivot
    pivot = wall
    return pivot

class unit_test(unittest.TestCase):
    def test(self):
        list = [8, 13, 2, 6, 1, 4]
        self.assertEqual([1, 2, 4, 6, 8, 13], quick_sort(list,0,len(list)-1))
        list = [8, 1, 2, 5, 10, 14, 7, 21]
        self.assertEqual([1, 2, 5, 7, 8, 10, 14, 21], quick_sort(list, 0, len(list) - 1))