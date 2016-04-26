__author__ = 'Minsuk Heo'
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

Example,
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import unittest

class TwoSum():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        dict = {}
        for i in xrange(n):
            if(nums[i] in dict):
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i

class MyTest(unittest.TestCase):
    def test(self):
        ts = TwoSum()
        self.assertEqual(ts.twoSum([2,7,11,15], 9), [0,1])
        self.assertEqual(ts.twoSum([2,7,11,15], 18), [1,2])