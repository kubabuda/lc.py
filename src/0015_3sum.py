from typing import *
# https://leetcode.com/problems/3sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n**2) time, O(n) memory
        # get exact count for every nums item
        itemcount = {}
        for n in nums:
            if n in itemcount:
                itemcount[n] += 1
            else:
                itemcount[n] = 1
        # for every item
        solutions = set()
        for n1 in itemcount:
            itemcount[n1] -= 1
            # do nested 2 sum
            for n2 in itemcount:
                if itemcount[n2] > 0:
                    itemcount[n2] -= 1
                    n3 = - n1 - n2
                    if n3 in itemcount and itemcount[n3] > 0:
                        sol = [n1, n2, n3]
                        sol.sort()
                        solutions.add((sol[0], sol[1], sol[2])) # add solution tuple to solutions set
                    itemcount[n2] += 1
            itemcount[n1] += 1

        return [[ni for ni in sol] for sol in solutions] # convert unique solutions set to list of lists

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase):     
    def testCases(self):
        param_list = [
            # ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
            # ([0,0,1], []),
            # ([0,0,0], [[0,0,0]]),
            ([-1,0,1],[[-1,0,1]]),
        ]
        for nums, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.threeSum(nums)
                # assert
                for r in result:
                    r.sort()
                result.sort()
                for e in expected:
                    e.sort()
                expected.sort()
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
